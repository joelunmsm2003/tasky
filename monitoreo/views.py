from ticket.models import *
from monitoreo.models import *
from django.http import HttpResponse, HttpResponseRedirect
import simplejson


from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.core import serializers
import simplejson
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse, HttpResponseRedirect
from ticket.models import *
import datetime
from django.core import serializers
import json  
import requests
import time
from ticket.models import Document
from ticket.forms import DocumentForm
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.core.mail import EmailMessage


def salirsistema(request):

  redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
  message = RedisMessage(str(request.user.first_name)+' se desconecto de Xiencias')
  redis_publisher.publish_message(message)

  logout(request)
  

  return HttpResponseRedirect("/equipo/"+str(id))

def sistema(request):


  return render_to_response('monitoreo/sistema.html', context_instance=RequestContext(request))


def login(request):

  if request.method=='POST':

    print json.loads(request.body)

    return HttpResponse('dato', content_type="application/json")

  return render_to_response('monitoreo/login.html', {},context_instance=RequestContext(request))



def input(request):

  id = request.user.id

  user = User.objects.get(id=id)

  print 'user',user

  return render_to_response('monitoreo/input.html', {'user':user},context_instance=RequestContext(request))

def version(request):

  if request.method == 'POST':

    dato = json.loads(request.body)['dato']

    id = request.user.id

    version = Usuarios.objects.get(id=id).version

    if int(version) == 1 :

      return HttpResponse('dato', content_type="application/json")

    return HttpResponse(dato, content_type="application/json")


def loger(request):

  if request.method =='POST':

    print request.POST

  return HttpResponse('data', content_type="application/json")


def nequipos(request):

  id = request.user.id

  empresa = Usuarios.objects.get(id=id).empresa

  equipos = Equipos.objects.filter(empresa=empresa).count()


  return HttpResponse(equipos, content_type="application/json")




def equipote(request,id):

  equipo = Equipos.objects.filter(empresa=id).order_by('-id')

  data = serializers.serialize('json', equipo)

  #return render_to_response('monitoreo/maquinas.html', {'data':data},content_type="application/json")

  return HttpResponse(data, content_type="application/json")


def maquinas(request):


  data = serializers.serialize('json', User.objects.all())

  #return render_to_response('monitoreo/maquinas.html', {'data':data},content_type="application/json")

  return HttpResponse(data, content_type="application/json")


def editar_equipo(request,id):

  equipo = Equipos.objects.get(id=id)

  if request.method == 'POST':

    equipo.name = request.POST['name']
    equipo.user = request.POST['user']
    equipo.password = request.POST['password']
    equipo.descripcion = request.POST['descripcion']
    equipo.ubicacion = request.POST['ubicacion']
    
    equipo.save()

    return HttpResponseRedirect("/equipo/"+str(equipo.empresa_id))
  

  
  


  return render_to_response('monitoreo/editar_equipo.html', {'equipo':equipo},
                              context_instance=RequestContext(request))


def empresa(request):

  grupo =User.objects.get(pk=request.user.id).groups.get()

  grupo=str(grupo)

  if grupo == 'Soporte':

    empresa = Empresa.objects.all().order_by('-id')

  else:

    emp = Usuarios.objects.get(id=request.user.id).empresa
    empresa = Empresa.objects.filter(name=emp)


  



  return render_to_response('monitoreo/home.html', {'empresa':empresa,'grupo':grupo},
                              context_instance=RequestContext(request))

def equipo(request,id):

  grupo =User.objects.get(pk=request.user.id).groups.get()

  grupo=str(grupo)

  empresa = Empresa.objects.get(id=id)

  equipo = Equipos.objects.filter(empresa=id).order_by('-id')

  if request.method == 'POST':

    name = request.POST['name']
    ip = request.POST['ip']
    user = request.POST['user']
    password = request.POST['pass']
    descripcion = request.POST['descripcion']
    ubicacion = request.POST['ubicacion']

    
    Equipos(empresa_id=id,name=name,ip=ip,user=user,password=password,descripcion=descripcion,ubicacion=ubicacion).save()

    return HttpResponseRedirect("/equipo/"+str(id))


  return render_to_response('monitoreo/equipo.html', {'grupo':grupo,'equipo':equipo,'empresa':empresa},
                              context_instance=RequestContext(request))



def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]


def equipos(request):


  equipos = Equipos.objects.all().values('id','empresa','name','ip','ubicacion','user').order_by('-id')

  equipos = ValuesQuerySetToDict(equipos)

  equipos = simplejson.dumps(equipos)

  return HttpResponse(equipos, content_type="application/json")




def eliminar_equipo(request,id,ide):

  
  equipo = Equipos.objects.get(id=id).delete()

  return HttpResponseRedirect("/equipo/"+str(ide))


def rango(request,ide):

  grupo =str(User.objects.get(pk=request.user.id).groups.get())
  red = Red.objects.all()
  tipo = Tipo.objects.all()
  caracteristica = Caracteristica.objects.all()

  if grupo == 'Clientes':

    empresa = Usuarios.objects.get(id=request.user.id).empresa
    rango=Rango.objects.filter(empresa_id=empresa)

  else:

    empresa = Empresa.objects.get(id=ide)
    rango=Rango.objects.filter(empresa_id=ide)

  if request.method == 'POST':

    ip = request.POST['ip']

    red = request.POST['red']

    tipo = request.POST['tipo']

    caracteristica = request.POST['caracteristica']

    Rango(ip=ip,red_id=red,tipo_id=tipo,caracteristica_id=caracteristica,empresa_id=ide).save()

    return HttpResponseRedirect("/rango/"+str(ide))




  return render_to_response('monitoreo/rango.html', {'red':red,'tipo':tipo,'caracteristica':caracteristica,'rango':rango,'empresa':empresa,'grupo':grupo},
                              context_instance=RequestContext(request))

def editar_rango(request,id):

  grupo =str(User.objects.get(pk=request.user.id).groups.get())
  rango = Rango.objects.get(id=id)
  red = Red.objects.all()
  tipo = Tipo.objects.all()
  caracteristica = Caracteristica.objects.all()

  red_s = str(rango.red)
  tipo_s = str(rango.tipo)
  caracteristica_s=str(rango.caracteristica)

  if request.method == 'POST':


    print request.POST

    rango.ip = request.POST['ip']
    
    rango.red_id = request.POST['red']
    
    rango.tipo_id = request.POST['tipo']
    rango.caracteristica_id = request.POST['caracteristica']
    
    
    rango.save()

    return HttpResponseRedirect("/rango/"+str(rango.empresa_id))
  


  return render_to_response('monitoreo/editar_rango.html', {'tipo_s':tipo_s,'caracteristica_s':caracteristica_s,'red_s':red_s,'grupo':grupo,'rango':rango,'red':red,'tipo':tipo,'caracteristica':caracteristica},
                              context_instance=RequestContext(request))



def editar_parametro(request,id):

  parametro = Parametro.objects.get(id=id)



  if request.method == 'POST':

    parametro.ip = request.POST['ip']
    parametro.puerto_origen = request.POST['puerto_origen']
    parametro.puerto_final = request.POST['puerto_final']
    parametro.tipo = request.POST['tipo']
    parametro.servicio = request.POST['servicio']
    parametro.user = request.POST['user']
    parametro.password = request.POST['password']
    
    parametro.save()

    return HttpResponseRedirect("/parametro/"+str(parametro.equipo_id)+"/"+str(parametro.equipo.empresa_id))
  


  return render_to_response('monitoreo/editar_parametro.html', {'parametro':parametro},
                              context_instance=RequestContext(request))

def eliminar_parametro(request,id,ide,idem):

  
  equipo = Parametro.objects.get(id=id).delete()

  return HttpResponseRedirect("/parametro/"+str(ide)+"/"+str(idem))


def eliminar_rango(request,id):

  
  empresa = Rango.objects.get(id=id).empresa_id
  Rango.objects.get(id=id).delete()

  return HttpResponseRedirect("/rango/"+str(empresa))





def parametro(request,id,ide):

  grupo =User.objects.get(pk=request.user.id).groups.get()

  grupo=str(grupo)

  empresa= Empresa.objects.get(id=ide)
  equipo = Equipos.objects.get(id=id)
  parametro = Parametro.objects.filter(equipo=id).order_by('-id')


  if request.method == 'POST':



    ip = request.POST['ip']
    puerto_origen = request.POST['puerto_origen']
    puerto_final = request.POST['puerto_final']
    tipo = request.POST['tipo']
    servicio = request.POST['servicio']
    user = request.POST['user']
    password = request.POST['password']

  
    Parametro(equipo_id=id,ip=ip,puerto_origen=puerto_origen,puerto_final=puerto_final,tipo=tipo,servicio=servicio,user=user,password=password).save()
    return HttpResponseRedirect("/parametro/"+str(id)+"/"+str(ide))


  return render_to_response('monitoreo/parametro.html', {'grupo':grupo,'empresa':empresa,'equipo':equipo,'parametro':parametro},
                              context_instance=RequestContext(request))


def servicio(request,idp,ide,idem):

  empresa= Empresa.objects.get(id=idem)
  equipo = Equipos.objects.get(id=ide)
  parametro = Parametro.objects.get(id=idp)
  servicio = Servicio.objects.filter(id=idp).order_by('-id')


  if request.method == 'POST':



    servicio = request.POST['servicio']
  
    Servicio(servicio=servicio).save()
    return HttpResponseRedirect("/servicio/"+str(idp)+"/"+str(ide)+"/"+str(idem))


  return render_to_response('monitoreo/servicio.html', {'servicio':servicio,'empresa':empresa,'equipo':equipo,'parametro':parametro},
                              context_instance=RequestContext(request))




'''

def index(request):
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       content = request.POST['content']

       post = Post(title=title)
       post.last_update = datetime.datetime.now() 
       post.content = content
       post.save()

    # Get all posts from DB
    posts = Post.objects 
    return render_to_response('index.html', {'Posts': posts},
                              context_instance=RequestContext(request))


def update(request):
    id = eval("request." + request.method + "['id']")
    post = Post.objects(id=id)[0]
    
    if request.method == 'POST':
        # update field values and save to mongo
        post.title = request.POST['title']
        post.last_update = datetime.datetime.now() 
        post.content = request.POST['content']
        post.save()
        template = 'index.html'
        params = {'Posts': Post.objects} 

    elif request.method == 'GET':
        template = 'update.html'
        params = {'post':post}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request):
    id = eval("request." + request.method + "['id']")

    if request.method == 'POST':
        post = Post.objects(id=id)[0]
        post.delete() 
        template = 'index.html'
        params = {'Posts': Post.objects} 
    elif request.method == 'GET':
        template = 'delete.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))
                              
    
'''