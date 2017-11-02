# -*- encoding: utf-8 -*-

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


#Contador de tareas en el header 


@csrf_exempt
def envio(request):


	url ="http://104.131.190.25/email/"

	origen = 'tasky@xiencias.org'

	to = ['joelunmsm@gmail.com']

	params = {'asunto':'Ticket Diloo','descripcion':'Eyes Illussion SMS','origen':origen,'destino':to}

	headers = {'Content-type': 'application/json', 'Accept': 'text/json'}

	r = requests.post(url, data=json.dumps(params), headers=headers)

	return HttpResponse(r, content_type="application/json")


@csrf_exempt
def enviolicencia(request):


	url ="http://104.131.190.25/email/"

	origen = 'tasky@xiencias.org'

	to = ['joelunmsm@gmail.com']

	params = {'asunto':'La dfdfd','descripcion':'Eyes Illussion SMS','origen':origen,'destino':to}

	headers = {'Content-type': 'application/json', 'Accept': 'text/json'}

	r = requests.post(url, data=json.dumps(params), headers=headers)

	return HttpResponse(r, content_type="application/json")



@csrf_exempt
def add_tarea(request):

	if request.method == 'POST':

		print request.GET

		username = request.GET['username']

		password = request.GET['password']
		
		user = authenticate(username=username, password=password)

		login(request,user)

		id = request.user.id

		username = request.user.username

		first_name = str(request.user.first_name)

		asunto = request.GET['asunto']
	
		tipo_id = request.GET['tipo']

		x=User.objects.get(id=id)

		grupo =x.groups.get()

		grupo= str(grupo)

		tipo = Tipo.objects.get(id=tipo_id)

		tipo=str(tipo.name)

		descripcion=request.GET['descripcion']

		fecha_inicio = datetime.datetime.today()

		empresa = Usuarios.objects.get(pk=id).empresa.id

		
	
	
		c=User.objects.get(pk=id).ticket_set.create(cancha='Soporte',empresa_id=empresa,cliente=username,asunto=asunto,tipo_id=tipo_id,descripcion=descripcion,fecha_inicio=fecha_inicio,estado_id=1)
		 
		c.save()

		c=Ticket.objects.get(cancha='Soporte',empresa_id=empresa,cliente_id=id,asunto=asunto,tipo_id=tipo_id,descripcion=descripcion,fecha_inicio=fecha_inicio,estado_id=1)

		totalticket = Ticket.objects.exclude(estado=4).count()

		asunto = asunto.encode('utf-8')

	
		redis_publisher = RedisPublisher(facility='foobar', users=['alvaro',str(username)])
		message = RedisMessage(str(request.user.first_name)+' agrego una tarea '+asunto+'-'+'at'+'-'+str(totalticket)+'-'+str(c.id))
		redis_publisher.publish_message(message)


		asunto = asunto.decode('utf-8')

		url ="http://xiencias.com:8000/mdetalle_ticket/"+str(c.id)

		s= str(fecha_inicio)

		fecha_inicio=str(s.split('.')[0])

		cuerpo =  chr(10)+chr(10)+'Asunto :  '+ asunto+ chr(10) + 'Generado por : ' + str(username)+chr(10)+ 'Tipo : ' +str(tipo)+chr(10)+'Descripcion : '+descripcion+chr(10)+'Fecha : '+str(fecha_inicio)+chr(10)+'Detalle de la tarea  : '+url

		email = str(User.objects.get(id=request.user.id).email)

		cuerpo = 'El usuario ' +first_name + ' creo un ticket, Hacer click aqui para ver mas detalle ' + url

		email = str(User.objects.get(id=request.user.id).email)

		url ="http://104.131.190.25/email/"

		params = {'asunto':asunto,'descripcion':cuerpo,'origen':'tasky@xiencias.org','destino':[email,'andyjo@xiencias.org','mayra@xiencias.org','alvarobencor@xiencias.org']}

		headers = {'Content-type': 'application/json', 'Accept': 'text/json'}

		r = requests.post(url, data=json.dumps(params), headers=headers)


		return HttpResponse('data', content_type="application/json")




def Values(grupo,sa,id):

	
	

	if grupo=='Soporte' :
	
		openn = Ticket.objects.filter(soporte_actual=sa,cancha='neutro').values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')
		opene = Ticket.objects.filter(soporte_actual=sa,cancha='Soporte',cliente=id).values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')
		
		users=User.objects.all()
		open1 = Ticket.objects.filter(soporte_actual=sa,cancha='Soporte').exclude(cliente=id).values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')
		answered = Ticket.objects.filter(soporte_actual=sa,cancha='Cliente').values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')


		
		open1c = Ticket.objects.filter(cliente=id,cancha='Soporte').exclude(soporte_actual=sa).values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')
		answeredc = Ticket.objects.filter(cliente=id,cancha='Cliente').values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')

		ac =answered.count()+answeredc.count()
		oc=open1.count()+open1c.count()+openn.count()

	
		

	if grupo=='Clientes' :


		opene = Ticket.objects.filter(soporte_actual=sa,cancha='Soporte',cliente=123).values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')
		
		id_e=Usuarios.objects.get(id=id).empresa

		users = User.objects.filter(groups__name__in=['Soporte'])
		open1 = Ticket.objects.filter(cliente=id,cancha='Cliente').values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')
		answered = Ticket.objects.filter(cliente=id,cancha='Soporte').values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')



		openn = Ticket.objects.filter(empresa_id=id_e,cancha='neutro').values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')	
		open1c = Ticket.objects.filter(empresa_id=id_e,cancha='Cliente').exclude(cliente=id).values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')
		answeredc = Ticket.objects.filter(empresa_id=id_e,cancha='Soporte').exclude(cliente=id).values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')


		ac =answered.count()+answeredc.count()
		oc=open1.count()+open1c.count()+openn.count()


	for i in range(len(opene)):

		fit = opene[i]['fecha_inicio']
		today = datetime.datetime.today()
		x=str(today-fit)
		y=x.split('.')[0]
		opene[i]['dif_fecha']=y
		ti=opene[i]['id']
		opene[i]['respuestas']=str(Evento.objects.filter(evento_id=ti).count())
		if opene[i]['soporte_actual']:
			opene[i]['soportea']=str(User.objects.get(username=opene[i]['soporte_actual']).first_name)
	

	for i in range(len(open1)):

		fit = open1[i]['fecha_inicio']
		today = datetime.datetime.today()
		x=str(today-fit)
		y=x.split('.')[0]
		open1[i]['dif_fecha']=y
		ti=open1[i]['id']
		open1[i]['respuestas']=str(Evento.objects.filter(evento_id=ti).count())
		if open1[i]['soporte_actual']:
			open1[i]['soportea']=str(User.objects.get(username=open1[i]['soporte_actual']).first_name)

	for i in range(len(openn)):

		fit = openn[i]['fecha_inicio']
		today = datetime.datetime.today()
		x=str(today-fit)
		y=x.split('.')[0]
		openn[i]['dif_fecha']=y
		ti=openn[i]['id']
		openn[i]['respuestas']=str(Evento.objects.filter(evento_id=ti).count())
		if openn[i]['soporte_actual']:
			openn[i]['soportea']=str(User.objects.get(username=openn[i]['soporte_actual']).first_name)


	for i in range(len(answered)):

		fit = answered[i]['fecha_inicio']
		today = datetime.datetime.today()
		x=str(today-fit)
		y=x.split('.')[0]
		answered[i]['dif_fecha']=y
		ti=answered[i]['id']
		answered[i]['respuestas']=str(Evento.objects.filter(evento_id=ti).count())
		if answered[i]['soporte_actual']:
			answered[i]['soportea']=str(User.objects.get(username=answered[i]['soporte_actual']).first_name)


	for i in range(len(open1c)):

		fit = open1c[i]['fecha_inicio']
		today = datetime.datetime.today()
		x=str(today-fit)
		y=x.split('.')[0]
		open1c[i]['dif_fecha']=y
		ti=open1c[i]['id']
		open1c[i]['respuestas']=str(Evento.objects.filter(evento_id=ti).count())
		if open1c[i]['soporte_actual']:
			open1c[i]['soportea']=str(User.objects.get(username=open1c[i]['soporte_actual']).first_name)

	for i in range(len(answeredc)):

		fit = answeredc[i]['fecha_inicio']
		today = datetime.datetime.today()
		x=str(today-fit)
		y=x.split('.')[0]
		answeredc[i]['dif_fecha']=y
		ti=answeredc[i]['id']
		answeredc[i]['respuestas']=str(Evento.objects.filter(evento_id=ti).count())
		if answeredc[i]['soporte_actual']:
			answeredc[i]['soportea']=str(User.objects.get(username=answeredc[i]['soporte_actual']).first_name)



	t = int(ac)+int(oc)

	tta=Ticket.objects.exclude(estado=4).count()

	data = {'opene':opene,'openn':openn,'users':users,'t':t, 'tta':tta, 'ac':ac,'oc':oc,'grupo':grupo,'open1':open1,'open1c':open1c,'answered':answered,'answeredc':answeredc}

	return data



@login_required(login_url="/logeate")
def chat(request):

	id = request.user.id

	grupo =User.objects.get(pk=id).groups.get()

	grupo= str(grupo)	

	sa = request.user.username

	data = Values(grupo,sa,id)


	return render(request, 'ticket/chat.html', {'users':data['users'],'grupo':grupo,'tta':data['tta'],'t':data['t'],'ac':data['ac'],'oc':data['oc'],'grupo':grupo})



@login_required(login_url="/ingresar")
def ticket(request,id):


	ticket = Ticket.objects.filter(id=id).values('id','descripcion')

	data_dict = ValuesQuerySetToDict(ticket)
	
	data_json = simplejson.dumps(data_dict)

	return HttpResponse(data_json, content_type="application/json")



@login_required(login_url="/logeate")
def chat1(request):


	if request.method == 'POST':

		print 'chat1'

		redis_publisher = RedisPublisher(facility='foobar', users=[request.POST.get('user')])
		message = RedisMessage(request.POST.get('emisor')+'-'+str(request.POST.get('message')))
		redis_publisher.publish_message(message)
		#Chat(user_id=id,name=request.POST.get('emisor'),chat=request.POST.get('message'),fecha=datetime.datetime.now()).save()
		return HttpResponse('OK')



@login_required(login_url="/logeate")
def chat2(request):

	if request.method == 'POST':

		id = request.user.id
		print 'chat2'
		'''
		Chat(user_id=id,name=request.POST.get('emisor'),chat=request.POST.get('message'),fecha=datetime.datetime.now()).save()
		'''
		return HttpResponse('OK')




@login_required(login_url="/logeate")
def ticketopen(request):

	if request.method == 'GET':

		id = request.user.id

		print id

		grupo =User.objects.get(pk=id).groups.get()

		grupo= str(grupo)

		sa = request.user.username

		data = Values(grupo,sa,id)

		print 'grupo',grupo

		
		return render(request,'ticket/ticketopen.html', {'opene':data['opene'],'openn':data['openn'],'users':data['users'],'open1c':data['open1c'],'answeredc':data['answeredc'],'tta':data['tta'],'grupo':grupo,'open':data['open1'],'answered':data['answered'],'t':data['t'],'ac':data['ac'],'oc':data['oc']})



def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]




@login_required(login_url="/logeate")
def ver_ticket(request):

	equipo = Ticket.objects.filter(id__gte=230)

	data = serializers.serialize('json', equipo)

  #return render_to_response('monitoreo/maquinas.html', {'data':data},content_type="application/json")

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/logeate")
def agregar(request):

	return render(request,'ticket/agregar.html', {})


@login_required(login_url="/logeate")
def webx(request):

	return render(request, 'web/index.html')


@login_required(login_url="/logeate")
def apiticket(request,asunto,descripcion):

	fecha = datetime.datetime.today()
	
	ticket=Ticket(cliente_id='14',asunto=str(asunto),descripcion=str(descripcion),fecha_inicio=fecha,tipo_id='1',estado_id='1')
	
	ticket.save()


	
	url = "http://xiencias.com:8000/mdetalle_ticket/"+ str(ticket.id)

	cuerpo =  chr(10)+chr(10)+'Asunto : '+ str(asunto)+ chr(10) + 'Generado por el Api Xiencias '+chr(10)+'Descripcion : '+str(descripcion)+chr(10)+'Fecha : '+str(fecha)+chr(10)+'URL : '+url

	#send_mail('Tarea '+ str(ticket.cliente)+' '+str(ticket.asunto), 'Se agrego un ticket'+str(cuerpo), 'tasky@xiencias.org', ['joelunmsm@gmail.com','xiencias@gmail.com','kcotrinav04@gmail.com'], fail_silently=False)
	
	
	print 'Gracias su ticket fue enviado, enviara un correo a xiencias@gmail.com'


	return render(request, 'ticket/movil.html')


@login_required(login_url="/logeate")
def push1(request):

	id = request.user.id
	username = request.user.username
	
	grupo =User.objects.get(pk=id).groups.get()
	grupo= str(grupo)

	if grupo=='Soporte' :

			open1 = Ticket.objects.filter(soporte_actual=request.user.username,cancha='Soporte').count()+Ticket.objects.filter(cliente=request.user.id,cancha='Cliente').values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').count()
			
			answered = Ticket.objects.filter(soporte_actual=request.user.username,cancha='Cliente').count()+Ticket.objects.filter(cliente=request.user.id,cancha='Soporte').values('estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').count()




	if grupo=='Clientes' :

			open1 = Ticket.objects.filter(cliente=request.user.id,cancha='Cliente').count()
			answered = Ticket.objects.filter(cliente=request.user.id,cancha='Soporte').count()



	tta=Ticket.objects.filter(estado=1).count()+Ticket.objects.filter(estado=2).count()+Ticket.objects.filter(estado=3).count()+Ticket.objects.filter(estado=5).count()+Ticket.objects.filter(estado=6).count()

	data = {'t_t':open1,'t_a' : answered,'t':open1+answered,'tta':tta}
	data = json.dumps(data)

	print data
	
	return HttpResponse(simplejson.dumps(data))



@login_required(login_url="/logeate")
def ticketscerrados(request):

	username = request.user.username
	
	id = request.user.id
	x=User.objects.get(pk=id)
	grupo =x.groups.get()
	grupo=str(grupo)

	if grupo=='Soporte' :

		ticket = Ticket.objects.filter(estado_id=4,soporte_actual=username).values('fecha_fin','estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-fecha_fin')

		ticketc = Ticket.objects.filter(estado_id=4,cliente_id=id).values('fecha_fin','estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-fecha_fin')

	if grupo=='Clientes' :

		id_e=Usuarios.objects.get(id=id).empresa

		ticket = Ticket.objects.filter(estado_id=4,cliente_id=id).values('fecha_fin','estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-fecha_fin')

		ticketc = Ticket.objects.filter(estado_id=4,empresa_id=id_e).values('fecha_fin','estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-fecha_fin')


	for i in range(len(ticket)):

		fit = ticket[i]['fecha_inicio']
		today = ticket[i]['fecha_fin']
		x=str(today-fit)
		y=x.split('.')[0]
		ticket[i]['dif_fecha']=y

	for i in range(len(ticketc)):

		fit = ticketc[i]['fecha_inicio']
		today = ticketc[i]['fecha_fin']
		x=str(today-fit)
		y=x.split('.')[0]
		ticketc[i]['dif_fecha']=y



	paginator = Paginator(ticket, 20) # Show 25 contacts per page

	page = request.GET.get('page')

	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
    # If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)


	sa = request.user.username

	data = Values(grupo,sa,id)

	
	return render(request, 'ticket/ticketscerrados.html', {'ticket':ticket,'ticketc':ticketc,'users':data['users'],'tta':data['tta'],'t':data['t'],'ac':data['ac'],'oc':data['oc'],'username':sa,'grupo':grupo,'contacts':contacts})



@login_required(login_url="/logeate")

def ver_usuario(request,id):

	usuario = User.objects.get(id=id)
	x=User.objects.get(pk=id)
	grupo =x.groups.get()
	grupo=str(grupo)
	username = request.user.username
	first_name = request.user.first_name

	usuarios = Usuarios.objects.get(id=id)
	telefono = usuarios.telefono_set.all()

	sa = request.user.username

	data = Values(grupo,sa,id)

	return render(request,'ticket/ver_usuario.html', {'users':data['users'],'tta':data['tta'],'t':data['t'],'ac':data['ac'],'oc':data['oc'],'telefono':telefono,'usuarios':usuarios,'first_name':first_name,'username':username,'usuario':usuario,'grupo':grupo})




@login_required(login_url="/logeate")
def telefono(request,id):

	usuario = User.objects.get(id=id)
	x=User.objects.get(pk=id)
	grupo =x.groups.get()
	grupo=str(grupo)
	username = request.user.username
	first_name = request.user.first_name

	usuarios = Usuarios.objects.get(id=id)
	telefono = usuarios.telefono_set.all()

	sa = request.user.username

	data = Values(grupo,sa,id)

	if request.method == 'POST':

		print request

		telefono = request.POST['telefono']
		tipo = request.POST['tipo']
		usuarios.telefono_set.create(telefono=telefono,tipo=tipo).save()
		redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
		message = RedisMessage(str(request.user.first_name)+' agrego un telefono')
		redis_publisher.publish_message(message)


		return HttpResponseRedirect("/telefono/"+str(id))

	return render(request,'ticket/telefono.html', {'users':data['users'],'ac':data['ac'],'oc':data['oc'],'telefono':telefono,'usuarios':usuarios,'first_name':first_name,'username':username,'usuario':usuario,'grupo':grupo})





def logeate(request):

	if request.user.is_authenticated():

 		return HttpResponseRedirect("/ticketopen")

	else:

		return render_to_response('ticket/logeate.html', context_instance=RequestContext(request))



def push(request):

	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)

	print user

	if str(user) == 'None':

		return HttpResponse(simplejson.dumps('Usuario o password incorrecto'))



	x= User.objects.get(username=str(user))


	groups=x.groups.get()
	groups =str(groups)

	if user is not None:
		if user.is_active:
			login(request, user)
			redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
			message = RedisMessage(str(request.user.first_name)+' se conecto a Xiencias')
			redis_publisher.publish_message(message)
			if (str(username)=='root'):

				return HttpResponse(simplejson.dumps('Admin')) 



			return HttpResponse(simplejson.dumps(groups)) 
		else:
			return HttpResponse(simplejson.dumps('Desactivado')) 
	else:
		return HttpResponse(simplejson.dumps('Usuario Incorrecto'))






def salir(request):

	redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
	message = RedisMessage(str(request.user.first_name)+' se desconecto de Xiencias')
	redis_publisher.publish_message(message)

	logout(request)
	

	return render_to_response('ticket/logeate.html', context_instance=RequestContext(request))



@login_required(login_url="/logeate")
def atender(request,id):

	ticket= Ticket.objects.get(id=id)
	url = "http://xiencias.com:8000/mdetalle_ticket/" + str(ticket.id)

	u=ticket.cliente
	email_cliente = str(u.email)
	email_root = str(User.objects.get(id=1).email)

	ticket_pendiente = Ticket.objects.filter(estado=1).order_by('-id')
	username = request.user.username
	id_soporte = request.user.id
	tipos=Tipo.objects.all()
	
	x=User.objects.get(username=username)
	
	grupo =x.groups.get()
	grupo= str(grupo)
	fecha_inicio = datetime.datetime.today()

	if ticket.estado_id ==1 :

		soporte=ticket.soporte_set.create(fecha_inicio=fecha_inicio,soporte_id=id_soporte)
		soporte.fecha_inicio = fecha_inicio
		soporte.save()
		ticket.asunto = ticket.asunto.encode('utf-8')


		redis_publisher = RedisPublisher(facility='foobar',users=['alvaro',str(ticket.cliente.username)])
		message = RedisMessage(str(request.user.first_name)+' atiende una tarea  '+ticket.asunto+'-'+'att'+'-'+str(ticket.id))
		redis_publisher.publish_message(message)

		ticket.estado_id = 2
		ticket.soporte_actual =request.user.username
		ticket.save()
		
		if ticket.soporte_actual == ticket.cliente.username:

			ticket.cancha = 'neutro'
			ticket.save()

		print ticket.cancha


		first_name = str(ticket.cliente.first_name)

		s= str(soporte.fecha_inicio)

		fecha_inicio=str(s.split('.')[0])


		ticket.asunto = ticket.asunto.decode('utf-8')
		
		cuerpo =  chr(10)+chr(10)+'Soporte : '+ str(soporte.soporte)+chr(10)+'Asunto : '+ ticket.asunto+ chr(10) + 'Cliente : ' + str(ticket.cliente)+chr(10)+ 'Tipo : ' +str(ticket.tipo)+chr(10)+'Fecha : '+str(fecha_inicio) +chr(10) + 'Detalle de la tarea  : '+ url

		#send_mail('Tarea '+ ticket.cliente.username+' '+ticket.asunto, 'La tarea fue atendido' + cuerpo, 'tasky@xiencias.org', [email_cliente,email_root], fail_silently=False)

	

	if ticket.estado_id ==5 :

		ticket.estado_id = 2
		ticket.save()

		ticket.asunto = ticket.asunto.encode('utf-8')

		redis_publisher = RedisPublisher(facility='foobar', users=['alvaro', str(ticket.cliente.username)])
		message = RedisMessage(str(request.user.first_name)+' atiende una tarea  '+ticket.asunto+'-'+'att'+'-'+str(ticket.id))
		redis_publisher.publish_message(message)

		s = ticket.soporte_set.all().order_by('-id')[:1]

		for s in s:
			s.fecha_inicio = datetime.datetime.today()
			s.save()


		first_name = str(ticket.cliente.first_name)

		ticket.asunto = ticket.asunto.decode('utf-8')

		cuerpo =  chr(10)+chr(10)+'Ticket Atendido  : '+chr(10)+'Asunto : '+ ticket.asunto+ chr(10) + 'Cliente : ' + str(ticket.cliente)+chr(10)+ 'Tipo : ' +str(ticket.tipo)+chr(10)+'Detalle dLa tarea : '+url

		#send_mail('Tarea '+ ticket.cliente.username+' '+ticket.asunto, 'La tarea fue atendido' + cuerpo, 'tasky@xiencias.org', [email_cliente,email_root], fail_silently=False)



	if ticket.estado_id ==6 :

		ticket.estado_id = 2
		ticket.save()

		ticket.asunto = ticket.asunto.encode('utf-8')

		redis_publisher = RedisPublisher(facility='foobar', users=['alvaro', str(ticket.cliente.username)])
		message = RedisMessage(str(request.user.first_name)+' atiende una tarea  '+ticket.asunto+'-'+'att'+'-'+str(ticket.id))
		redis_publisher.publish_message(message)

		first_name = str(ticket.cliente.first_name)

		s = ticket.soporte_set.all().order_by('-id')[:1]
		for s in s:
			s.fecha_inicio = datetime.datetime.today()
			s.save()


		ticket.asunto = ticket.asunto.decode('utf-8')

		cuerpo =  chr(10)+chr(10)+'Ticket Atendido  : '+chr(10)+'Asunto : '+ ticket.asunto+ chr(10) + 'Cliente : ' + str(ticket.cliente)+chr(10)+ 'Tipo : ' +str(ticket.tipo)+chr(10)+' Detalle de la tarea  : '+url

		#send_mail('Tarea '+ ticket.cliente.username+' '+ ticket.asunto, 'La tarea fue atendido' + cuerpo, 'tasky@xiencias.org', [email_cliente,email_root], fail_silently=False)


	


	return HttpResponseRedirect("/mdetalle_ticket/"+id+"/")

@login_required(login_url="/logeate")
def cerrar(request,id):

	ticket= Ticket.objects.get(id=id)
	ticket.estado_id = 3
	



	ticket.save()
	redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
	message = RedisMessage(str(request.user.first_name)+' cerro una tarea  '+ticket.asunto)
	redis_publisher.publish_message(message)

	s = ticket.soporte_set.all().order_by('-id')[:1]
	for s in s:
		s.fecha_inicio = datetime.datetime.today()
		s.save()

	return HttpResponseRedirect("/mdetalle_ticket/"+str(id))

@login_required(login_url="/logeate")
def reasignar(request,id,id_ticket):

	id_ticket= str(id_ticket)
	ticket = Ticket.objects.get(id=id_ticket)
	ticket.estado_id=6
	ticket.save()

	ticket.asunto = ticket.asunto.encode('utf-8')

	redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
	message = RedisMessage(str(request.user.first_name)+' reasigno una tarea  '+ticket.asunto)
	redis_publisher.publish_message(message)

	idlog= request.user.id

	soporte= Soporte.objects.get(id=id)
	

	user_soporte = User.objects.filter(groups__name='Soporte').exclude(id=idlog)


	
	tipo=Tipo.objects.all()
	username = request.user.username
	x=User.objects.get(username=username)
	
	grupo =x.groups.get()
	grupo= str(grupo)

	sa = request.user.username

	data = Values(grupo,sa,id)

	return render(request,'ticket/reasignar.html', {'users':data['users'],'tta':data['tta'],'t':data['t'],'ac':data['ac'],'oc':data['oc'],'id_ticket':id_ticket ,'user_soporte':user_soporte,'soporte':soporte,'username':username,'grupo':grupo,'tipo':tipo})

@login_required(login_url="/logeate")
def asignar_post_gilda_new(request,soporte,ticket):

	user_soporte = User.objects.get(id=soporte)
	email = str(user_soporte.email)

	fecha_inicio = datetime.datetime.today()

	ticket = Ticket.objects.get(id=ticket)
	ticket.cancha ="Soporte"

	url = "http://xiencias.com/:8000/mdetalle_ticket/" + str(ticket.id)

	ticket.estado_id = 5
	ticket.soporte_actual = str(user_soporte.username)
	ticket.save()

	username = request.user.username
	x=User.objects.get(username=username)
	
	grupo =x.groups.get()
	grupo= str(grupo)

	print ('soporte',soporte)


	if grupo=='Soporte' :

		tt=Ticket.objects.filter(cliente_id=soporte).exclude(estado_id=4).count()+Ticket.objects.filter(soporte_actual=user_soporte.username).exclude(estado_id=4).count()
		tts=Ticket.objects.filter(cliente_id=soporte,cancha='Soporte').exclude(estado_id=4).count()+Ticket.objects.filter(soporte_actual=user_soporte.username,cancha='Soporte').exclude(estado_id=4).count()
	
	ticket.asunto = ticket.asunto.encode('utf-8')

	redis_publisher = RedisPublisher(facility='foobar', users=user_soporte.username)
	message = RedisMessage('Admin'+' asigno una tarea  '+str(ticket.asunto)+'-'+'ast'+'-'+str(ticket.id)+'-'+str(ticket.asunto))
	redis_publisher.publish_message(message)

	first_name = str(ticket.cliente.first_name)

	sa = ticket.soporte_set.create(fecha_inicio=fecha_inicio,soporte_id=soporte)
	

	s= str(sa.fecha_inicio)

	fecha_inicio=str(s.split('.')[0])

	ticket.asunto = ticket.asunto.decode('utf-8')

	cuerpo =  chr(10)+chr(10)+'Soporte asignado  : '+ str(sa.soporte.username)+chr(10)+'Tarea'+chr(10)+'Asunto : '+ ticket.asunto+ chr(10) + 'Cliente : ' + ticket.cliente.username+chr(10)+ 'Tipo : ' +str(ticket.tipo)+chr(10)+'Fecha : '+str(fecha_inicio) +chr(10)+'Detalle de la tarea  : '+url

	##send_mail('Tarea '+ ticket.cliente.username+' '+ticket.asunto, 'La tarea fue asignado' + cuerpo, 'tasky@xiencias.org', [email], fail_silently=False)

	return HttpResponseRedirect("/gilda")

@login_required(login_url="/logeate")
def reasignar_post_gilda_new(request,soporte_act,ticket,soporte):


	sa = Soporte.objects.get(id=soporte_act)
	print sa
	
	sa.fecha_inicio = datetime.datetime.today()
	sa.soporte_id = soporte

	sa.save()


	user =User.objects.get(username=sa.soporte)
	email=str(user.email)
	print email

	user_soporte = User.objects.get(id=soporte)
	

	fecha_inicio = datetime.datetime.today()

	ticket = Ticket.objects.get(id=ticket)
	ticket.estado_id = 5
	ticket.soporte_actual = str(user_soporte.username)
	ticket.save()

	url = "http://xiencias.com:8000/mdetalle_ticket/" + str(ticket.id)

	first_name = str(ticket.cliente.first_name)

	s= str(sa.fecha_inicio)

	fecha_inicio=str(s.split('.')[0])

	ticket.asunto = ticket.asunto.encode('utf-8')
	ticket.descripcion = ticket.descripcion.encode('utf-8')

	redis_publisher = RedisPublisher(facility='foobar', users=sa.soporte.username)
	message = RedisMessage(' reasigno una tarea  '+ticket.asunto+'-'+'ast'+'-'+str(ticket.id)+'-'+ticket.asunto)
	redis_publisher.publish_message(message)

	cuerpo =  chr(10)+chr(10)+'Soporte reasignado  : '+ str(sa.soporte)+chr(10)+'Tarea'+chr(10)+'Asunto : '+ ticket.asunto+ chr(10) + 'Cliente : ' + str(ticket.cliente)+chr(10)+ 'Tipo : ' +str(ticket.tipo)+chr(10)+'Descripcion : '+str(ticket.descripcion)+chr(10)+'Fecha : '+str(fecha_inicio) +chr(10)+'Detalle de la tarea  : '+url

	ticket.asunto = ticket.asunto.decode('utf-8')
		
	##send_mail('Tarea '+ str(ticket.cliente)+' '+ticket.asunto, 'La tarea fue reasignado' + cuerpo, 'tasky@xiencias.org', [email], fail_silently=False)


	

	return HttpResponseRedirect("/gilda")


@login_required(login_url="/logeate")
def asignar_gilda(request,id_ticket):

	ticket = Ticket.objects.get(id=id_ticket)
	user_soporte = User.objects.filter(groups__name='Soporte')
	username = request.user.username
	tipo=Tipo.objects.all()
	x=User.objects.get(username=username)
	grupo =x.groups.get()
	grupo= str(grupo)

	if grupo=='Soporte' :

		sa = request.user.username

		data = Values(grupo,sa,request.user.id)

		today = datetime.datetime.today()
				
				
		z=str(today-ticket.fecha_inicio).split('.')[0]

		return render(request,'ticket/asignar_gilda.html', {'users':data['users'],'z':z,'tta':data['tta'],'ac':data['ac'],'oc':data['oc'],'t':data['t'],'ticket':ticket,'user_soporte':user_soporte,'username':username,'grupo':grupo,'tipo':tipo})

	else:

		return HttpResponseRedirect("/logeate")



@login_required(login_url="/logeate")
def reasignar_gilda(request,id_ticket):

	
	ticket = Ticket.objects.get(id=id_ticket)


	soporte = ticket.soporte_set.all().values('id').annotate(dcount=Max('fecha_inicio'))
	soporte = soporte[0]['id']
	user_soporte = User.objects.filter(groups__name='Soporte')

	username = request.user.username
	tipo=Tipo.objects.all()
	x=User.objects.get(username=username)
	
	grupo =x.groups.get()
	grupo= str(grupo)

	if grupo=='Soporte' :

		sa = request.user.username

		data = Values(grupo,sa,request.user.id)

		today = datetime.datetime.today()
			
				
		z=str(today-ticket.fecha_inicio).split('.')[0]


		return render(request,'ticket/reasignar_gilda.html', {'users':data['users'],'z':z,'t':data['t'],'ac':data['ac'],'oc':data['oc'],'tta':data['tta'],'soporte':soporte,'ticket':ticket,'user_soporte':user_soporte,'username':username,'grupo':grupo,'tipo':tipo})

	else:

		return HttpResponseRedirect("/logeate")


@login_required(login_url="/logeate")
def gilda(request):


	if request.user.is_authenticated():

		redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
		message = RedisMessage('Se conecto el usuario '+str(request.user.first_name))
		# and somewhere else
		redis_publisher.publish_message(message)

		ticket_nuevo= Ticket.objects.filter(estado=1).exclude(empresa__name='Xiencias-Adm').values('tipo__name','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-id')
		ticket_atendido= Soporte.objects.filter(ticket__estado=2,fecha_fin=None).exclude(ticket__empresa__name='Xiencias-Adm').values('ticket__tipo__name','ticket__soporte_actual','ticket__estado','fecha_inicio','ticket__cliente__first_name','soporte','soporte__first_name','soporte__username','ticket__fecha_inicio','ticket_id','ticket__asunto').annotate(dcount=Max('fecha_inicio')).order_by('-id')
		ticket_preatendido= Soporte.objects.filter(ticket__estado=5).exclude(ticket__empresa__name='Xiencias-Adm').values('ticket__tipo__name','ticket__estado','fecha_inicio','ticket__cliente__first_name','soporte__username','soporte__first_name','ticket__fecha_inicio','ticket_id','ticket__asunto').annotate(dcount=Max('fecha_inicio')).order_by('-id')
		ticket_cerrados= Soporte.objects.filter(ticket__estado=3,fecha_fin=None).exclude(ticket__empresa__name='Xiencias-Adm').values('ticket__tipo__name','ticket__estado','fecha_inicio','ticket__cliente__first_name','soporte__username','soporte__first_name','ticket__fecha_inicio','ticket_id','ticket__asunto').annotate(dcount=Max('fecha_inicio')).order_by('-id')
		ticket_reasignado= Soporte.objects.filter(ticket__estado=6,fecha_fin=None).exclude(ticket__empresa__name='Xiencias-Adm').values('ticket__tipo__name','ticket__estado','fecha_inicio','ticket__cliente__first_name','soporte__username','soporte__first_name','ticket__fecha_inicio','ticket_id','ticket__asunto').annotate(dcount=Max('fecha_inicio')).order_by('-id')
		
		for i in range(len(ticket_nuevo)):

			
			fis = ticket_nuevo[i]['fecha_inicio']
			today = datetime.datetime.today()
			z=str(today-fis).split('.')[0]

			if int(len(str(today-fis).split('day'))) != 1 :

				z= str(today-fis).split(',')[0]
			
			ticket_nuevo[i]['dif_fecha']=z
			ticket_nuevo[i]['estado']='N'

			
		for i in range(len(ticket_preatendido)):

			fit = ticket_preatendido[i]['ticket__fecha_inicio']
			fis = ticket_preatendido[i]['fecha_inicio']

			today = datetime.datetime.today()
		
			
			
			y=str(today-fit).split('.')[0]

			z=str(today-fis).split('.')[0]


			if int(len(str(today-fit).split('day'))) != 1 :

				y= str(today-fit).split(',')[0]

			if int(len(str(today-fis).split('day'))) != 1 :

				z= str(today-fis).split(',')[0]
		
			ticket_preatendido[i]['dif_fecha']=y
			ticket_preatendido[i]['fecha']=z
			ticket_preatendido[i]['ticket__estado']='AS'

		for i in range(len(ticket_atendido)):

			fit = ticket_atendido[i]['ticket__fecha_inicio']
			fis = ticket_atendido[i]['fecha_inicio']
		
			today = datetime.datetime.today()
			
			
			y=str(today-fit).split('.')[0]

			z=str(today-fis).split('.')[0]


			if int(len(str(today-fit).split('day'))) != 1 :

				y= str(today-fit).split(',')[0]

			if int(len(str(today-fis).split('day'))) != 1 :

				z= str(today-fis).split(',')[0]

			ticket_atendido[i]['dif_fecha']=y
			ticket_atendido[i]['fecha']=z
			ticket_atendido[i]['ticket__estado'] = 'AT'

		for i in range(len(ticket_reasignado)):

			fit = ticket_reasignado[i]['ticket__fecha_inicio']
			fis = ticket_reasignado[i]['fecha_inicio']
		
			today = datetime.datetime.today()
			
		
			y=str(today-fit).split('.')[0]

			z=str(today-fis).split('.')[0]


			if int(len(str(today-fit).split('day'))) != 1 :

				y= str(today-fit).split(',')[0]

			if int(len(str(today-fis).split('day'))) != 1 :

				z= str(today-fis).split(',')[0]


			ticket_reasignado[i]['dif_fecha']=y
			ticket_reasignado[i]['fecha']=z
			ticket_reasignado[i]['ticket__estado'] = 'R'


		for i in range(len(ticket_cerrados)):

			fit = ticket_cerrados[i]['ticket__fecha_inicio']
			fis = ticket_cerrados[i]['fecha_inicio']
		
			today = datetime.datetime.today()
			
			
			y=str(today-fit).split('.')[0]

			z=str(today-fis).split('.')[0]


			if int(len(str(today-fit).split('day'))) != 1 :

				y= str(today-fit).split(',')[0]

			if int(len(str(today-fis).split('day'))) != 1 :

				z= str(today-fis).split(',')[0]


			ticket_cerrados[i]['dif_fecha']=y
			ticket_cerrados[i]['fecha']=z
			ticket_cerrados[i]['ticket__estado'] = 'V'
			

		user_soporte = User.objects.filter(groups__name='Soporte')

		username = request.user.username
		tipo=Tipo.objects.all()
		x=User.objects.get(username=username)
		
		grupo =x.groups.get()
		grupo= str(grupo)

		if grupo == 'Soporte':
	
			data = Values(grupo,username,request.user.id)

			today = datetime.datetime.today()

			return render(request,'ticket/gilda.html', {'users':data['users'],'tta':data['tta'],'ac':data['ac'],'oc':data['oc'],'t':data['t'],'ticket_reasignado':ticket_reasignado,'ticket_cerrados':ticket_cerrados,'ticket_preatendido':ticket_preatendido,'ticket_atendido':ticket_atendido,'ticket_nuevo':ticket_nuevo,'user_soporte':user_soporte,'username':username,'grupo':grupo,'tipo':tipo})

		if grupo == 'Clientes':

			return HttpResponseRedirect("/logeate")
		

	else:



		return HttpResponseRedirect("/logeate")

@login_required(login_url="/logeate")
def reasignar_add(request):

	if request.method == 'POST':

		form = FormTicket(request.POST)
		username = request.user.username
		soporte_user = request.POST['soporte']
		
		id_ticket = request.POST['id_ticket']

		titulo = request.POST['descripcion']

		ticket = Ticket.objects.get(id=id_ticket)
		first_name = str(ticket.cliente.first_name)

		id = request.POST['id']
		fecha_inicio = datetime.datetime.today()
		soporte = Soporte.objects.get(id=id)
		


		fecha_fin = datetime.datetime.today()
		soporte.fecha_fin = fecha_fin

		soporte.save()
	

		



		soporte_r= ticket.soporte_set.create(fecha_inicio=fecha_fin,soporte_id=soporte_user,titulo=titulo)


		ticket.soporte_actual = str(soporte_r.soporte)
		ticket.cancha ="Soporte"

		ticket.save()

		url = "http://xiencias.com:8000/mdetalle_ticket/" + str(ticket.id)


		s= str(soporte.fecha_inicio)

		fecha_inicio=str(s.split('.')[0])

		ticket.asunto = ticket.asunto.encode('utf-8')

		redis_publisher = RedisPublisher(facility='foobar', users=str(soporte_r.soporte))
		message = RedisMessage(' Te asigno una tarea  '+str(ticket.asunto)+'-'+'ast'+'-'+str(ticket.id)+'-'+ticket.asunto)
		redis_publisher.publish_message(message)

		redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
		message = RedisMessage(str(request.user.first_name)+' reasigno una tarea  '+ticket.asunto)
		redis_publisher.publish_message(message)

		ticket.asunto = ticket.asunto.decode('utf-8')

		email = User.objects.get(id = soporte_user).email

		cuerpo = 'Un ticket se te reasigno, Hacer click aqui para ver mas detalle ' + url

		email = str(User.objects.get(id=request.user.id).email)

		url ="http://104.131.190.25/email/"

		params = {'asunto':asunto,'descripcion':cuerpo,'origen':'tasky@xiencias.org','destino':[email]}

		headers = {'Content-type': 'application/json', 'Accept': 'text/json'}

		r = requests.post(url, data=json.dumps(params), headers=headers)
		
		x=User.objects.get(username=username)

		grupo =x.groups.get()
		grupo= str(grupo)


		return HttpResponseRedirect("/ticketopen")


@login_required(login_url="/logeate")
def validar(request,id):

	ticket= Ticket.objects.get(id=id)
	ticket.estado_id = 4
	fecha_fin = datetime.datetime.today()
	ticket.fecha_fin = fecha_fin
	username = request.user.username
	first_name = str(ticket.cliente.first_name)
	x=User.objects.get(username=username)
	grupo =x.groups.get()
	grupo= str(grupo)
	ticket.cancha ='Cerrado'
	ticket.save()

 	ticket.asunto = ticket.asunto.encode('utf-8')

	redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
	message = RedisMessage(str(request.user.first_name)+' cerro una tarea  '+ticket.asunto)
	redis_publisher.publish_message(message)

	user = User.objects.get(username=ticket.cliente)

	if user.username == username :

		if ticket.soporte_actual != '' :
			email= User.objects.get(username=ticket.soporte_actual).email
		else:
			email='xiencias@gmail.com'
	else:
		email= User.objects.get(username=ticket.cliente).email


	ta = Ticket.objects.filter(estado_id=5)

	ta=ta.count()

	s= str(ticket.fecha_inicio)

	fecha_inicio=str(s.split('.')[0])

	url = "http://xiencias.com:8000/mdetalle_ticket/"+str(ticket.id)

	

	redis_publisher = RedisPublisher(facility='foobar', users=[str(ticket.cliente.username), str(ticket.soporte_actual)])
	message = RedisMessage(str(request.user.first_name)+' cerro la tarea '+ticket.asunto+'-'+'ct'+'-'+str(ticket.id)+'-'+ticket.asunto)
	redis_publisher.publish_message(message)

	ticket.asunto = ticket.asunto.decode('utf-8')

	cuerpo = 'Un ticket fue cerrado , Hacer click aqui para ver mas detalle ' + url

	email = str(User.objects.get(id=request.user.id).email)

	url ="http://104.131.190.25/email/"

	params = {'asunto':'Ticket Cerrado','descripcion':cuerpo,'origen':'tasky@xiencias.org','destino':[email,'mayra@xiencias.org','andyjo@xiencias.org']}

	headers = {'Content-type': 'application/json', 'Accept': 'text/json'}

	r = requests.post(url, data=json.dumps(params), headers=headers)

	#send_mail('Tarea '+ str(ticket.cliente.username)+' '+ticket.asunto, 'La tarea fue cerrado' + cuerpo, 'tasky@xiencias.org', [email], fail_silently=False)


	return HttpResponseRedirect("/ticketopen")




@login_required(login_url="/logeate")

def mdetalle_ticket(request,id):

	if request.user.is_authenticated():

		ticket= Ticket.objects.get(id=id)
		
		

		if Soporte.objects.filter(ticket_id=id).order_by('-id')[:1]:

			soportes = Soporte.objects.filter(ticket_id=id).order_by('-id')[:1][0]

		else:

			soportes = ""	
				
		evento = Evento.objects.filter(evento_id=id).values('id','evento','user','user__first_name','name','fecha_inicio','comentario')

		for i in range(len(evento)):

			n =Document_Event.objects.filter(evento_id=evento[i]['id']).count()
		
			evento[i]['files']=n

		id = request.user.id
		user = User.objects.get(id=id)
		username = request.user.username
		
		tipos=Tipo.objects.all()
		x=User.objects.get(username=username)
		grupo =x.groups.get()
		grupo= str(grupo)
		estado= str(ticket.estado)

		fit=ticket.fecha_inicio
		today = datetime.datetime.today()

		print ticket.estado

		if str(ticket.estado) == 'Cerrado':

			x=str(ticket.fecha_fin-fit)
			espera=x.split('.')[0]

		else:

			x=str(today-fit)
			espera=x.split('.')[0]

		event = Evento.objects.count()
	

		data = Values(grupo,username,id)

		return render(request, 'ticket/mdetalle_ticket.html', {'users':data['users'],'tta':data['tta'],'t':data['t'],'ac':data['ac'],'oc':data['oc'],'evento':evento,'user':user,'espera':espera,'estado':estado,'event':event,'soportes':soportes,'username':username,'grupo':grupo,'tipos':tipos,'ticket':ticket})


	else:

		return HttpResponseRedirect("/logeate")


@login_required(login_url="/logeate")
def eventos(request,id_ticket):

	if request.method == 'GET':

		id = request.user.id

		print request.GET

		grupo =User.objects.get(pk=id).groups.get()

		grupo= str(grupo)

	
		evento = Evento.objects.filter(evento_id=id_ticket).values('id','evento','user','user__first_name','name','comentario').order_by('-id')

		
		fmt = '%Y-%m-%d %H:%M:%S %Z'

		for i in range(len(evento)):

			evento[i]['fecha'] = Evento.objects.get(id=evento[i]['id']).fecha_inicio.strftime(fmt)
			evento[i]['files'] = Document_Event.objects.filter(evento_id=evento[i]['id']).count()



		

		data_dict = ValuesQuerySetToDict(evento)

		data_json = json.dumps(data_dict)

		return HttpResponse(data_json, content_type="application/json")



		
@login_required(login_url="/logeate")
def evento_add(request):

	
	if request.method == 'POST':

		ticket = request.POST['id_ticket']
		
		user = 	request.user.id	

		username = 	request.user.username
		first_name	= request.user.first_name
		name = request.POST['name']
		fecha_inicio = datetime.datetime.today()

		x=User.objects.get(username=username)
		grupo =x.groups.get()
		grupo= str(grupo)
		ix = request.POST['cont']		

		print ('ix',ix)

		doc= chr(10)


		ticket = Ticket.objects.get(id=ticket)
		email = ticket.cliente.email
		
		if grupo=='Soporte':
			ticket.cancha='Cliente'
		else:
			ticket.cancha='Soporte'

		
		creti = str(User.objects.get(username=ticket.cliente.username).groups.get())

		ticket.asunto = ticket.asunto.encode('utf-8')

		if creti=='Soporte':

			

			if username == ticket.cliente.username:

				ticket.cancha='Soporte'

				redis_publisher = RedisPublisher(facility='foobar', users=ticket.soporte_actual)
				message = RedisMessage(str(request.user.first_name)+' agrego una respuesta a la tarea '+ticket.asunto+'-'+'ar'+'-'+str(ticket.id)+'-'+str(ticket.asunto))
				redis_publisher.publish_message(message)

			else:

				ticket.cancha='Cliente'
				
				redis_publisher = RedisPublisher(facility='foobar', users=ticket.soporte_actual)
				message = RedisMessage(str(request.user.first_name)+' agrego una respuesta a la tarea '+ticket.asunto+'-'+'ar'+'-'+str(ticket.id)+'-'+str(ticket.asunto))
				redis_publisher.publish_message(message)





		ticket.save()


		if grupo == 'Soporte':

	

			redis_publisher = RedisPublisher(facility='foobar', users=[ticket.cliente.username,ticket.soporte_actual])
			message = RedisMessage(str(request.user.first_name)+' agrego una respuesta a la tarea '+ticket.asunto+'-'+'ar'+'-'+str(ticket.id)+'-'+str(ticket.asunto))
			redis_publisher.publish_message(message)

		if grupo == 'Clientes':
			
			redis_publisher = RedisPublisher(facility='foobar', users=[ticket.cliente.username,ticket.soporte_actual])
			message = RedisMessage(str(request.user.first_name)+' agrego una respuesta a la tarea '+ticket.asunto+'-'+'ar'+'-'+str(ticket.id)+'-'+str(ticket.asunto))
			redis_publisher.publish_message(message)


	
		print ticket.cancha

		
		xx=0
	
		s=ticket.soporte_set.all().order_by('-id')[:1]

		print ('s',s)

		for s in s:
			emails=str(s.soporte.email)
			xx=1
				
				


		evento=ticket.evento_set.create(fecha_inicio=fecha_inicio,name=name,user_id=user)

		print request.FILES

	
		
		i=1
		
		for i in range (1, int(ix)+1):
		
			newdoc = Document_Event(docfile = request.FILES['docfile'+str(i)],evento_id=evento.id,user_id=user)
			
			print request.FILES['docfile'+str(i)]

			print evento.id

			print user

			newdoc.save()

			doc = doc + 'http://xiencias.com/html/'+str(newdoc.docfile)+chr(10)

		s= str(evento.fecha_inicio)

		fecha_inicio=str(s.split('.')[0])

		url ="http://xiencias.com:8000/mdetalle_ticket/"+str(ticket.id)

		ticket.asunto = ticket.asunto.decode('utf-8')
		
		cuerpo =  chr(10)+chr(10)+'Respuesta : '+ evento.name+chr(10)+'Tarea'+chr(10)+'Asunto : '+ ticket.asunto+ chr(10) + 'Cliente : ' + username+chr(10)+ 'Tipo : ' +str(ticket.tipo)+chr(10)+'Fecha : '+str(fecha_inicio) +chr(10)+'Archivos adjuntos : ' + doc +'Detalle de la tarea  : '+str(url)

		'''
		if xx==0:
			
			#send_mail('Tarea '+ str(ticket.cliente.username)+' '+ticket.asunto, 'Se agrego una nueva respuesta por ' +str(first_name)+ cuerpo, 'tasky@xiencias.org', [email,'soporte_xiencias@xiencias.org'], fail_silently=False)
		else:
			#send_mail('Tarea '+ str(ticket.cliente.username)+' '+ticket.asunto, 'Se agrego una nueva respuesta por ' +str(first_name)+ cuerpo, 'tasky@xiencias.org', [email,emails], fail_silently=False)
		
		'''

		cuerpo = 'Se agrego una nueva respuesta , Hacer click aqui para ver mas detalle ' + url

		email = str(User.objects.get(id=request.user.id).email)

		url ="http://104.131.190.25/email/"

		params = {'asunto':ticket.asunto,'descripcion':cuerpo,'origen':'tasky@xiencias.org','destino':[email,'andyjo@xiencias.org','mayra@xiencias.org','alvarobencor@xiencias.org']}

		headers = {'Content-type': 'application/json', 'Accept': 'text/json'}

		r = requests.post(url, data=json.dumps(params), headers=headers)


		return HttpResponseRedirect("/mdetalle_ticket/"+str(ticket.id))



@login_required(login_url="/logeate")
def agregar_ticket_movil(request):
    # Handle file upload
	
	username = request.user.username
	tipos=Tipo.objects.all()


	if request.method == 'POST':

		id = request.user.id
		form = DocumentForm(request.POST, request.FILES)

		username = request.user.username
		first_name = str(request.user.first_name)

		asunto = request.POST['asunto']
	
		tipo_id = request.POST['tipo']



		x=User.objects.get(username=username)
		grupo =x.groups.get()
		grupo= str(grupo)

		tipo = Tipo.objects.get(id=tipo_id)
		tipo=str(tipo.name)
		descripcion=request.POST['descripcion']


		fecha_inicio = datetime.datetime.today()

		
		#estado 1=Nuevo	2=Atendido 3=Prueba 4=Cerrado
		#tipo 1=Incidencia 2=Requerimento
		if grupo=='Soporte':
			empresa= request.POST['cliente']
	
		else:
			empresa=2	
	
		c=User.objects.get(pk=id).ticket_set.create(cancha='Soporte',empresa_id=empresa,cliente=username,asunto=asunto,tipo_id=tipo_id,descripcion=descripcion,fecha_inicio=fecha_inicio,estado_id=1)
		 

		c.save()

		c=Ticket.objects.get(cancha='Soporte',empresa_id=empresa,cliente_id=id,asunto=asunto,tipo_id=tipo_id,descripcion=descripcion,fecha_inicio=fecha_inicio,estado_id=1)

		totalticket = Ticket.objects.exclude(estado=4).count()

		asunto = asunto.encode('utf-8')


		if c.empresa.name == 'Xiencias-Adm':

			c.soporte_actual = 'gila'
			c.estado_id =2 
			c.save()

			
			redis_publisher = RedisPublisher(facility='foobar', users='gila')
			message = RedisMessage(str(request.user.first_name)+' agrego una tarea '+asunto+'-'+'atg'+'-'+str(totalticket)+'-'+str(c.id))
			redis_publisher.publish_message(message)

		else:

			
			cli =Usuarios.objects.filter(empresa_id=c.empresa.id)[:1]

			for cli in cli:

				cliti = User.objects.get(id=cli.id).first_name
				print cliti

			redis_publisher = RedisPublisher(facility='foobar', users=['alvaro',str(username),cliti])
			message = RedisMessage(str(request.user.first_name)+' agrego una tarea '+asunto+'-'+'at'+'-'+str(totalticket)+'-'+str(c.id))
			redis_publisher.publish_message(message)

		asunto = asunto.decode('utf-8')

		url ="http://xiencias.com:8000/mdetalle_ticket/"+str(c.id)

		ix = request.POST['cont']

		doc=chr(10)	

		print request.FILES			

		for a in range (1, int(ix)+1):

			print request.FILES['docfile'+str(a)]
			
			newdoc = Document(docfile = request.FILES['docfile'+str(a)],ticket_id=c.id,user_id=id)
			newdoc.save()

			print newdoc.docfile

			doc = doc + 'http://xiencias.com/html/'+str(newdoc.docfile)+chr(10)
			

		s= str(fecha_inicio)

		fecha_inicio=str(s.split('.')[0])

		cuerpo = 'El usuario ' +first_name + ' creo un ticket, Hacer click aqui para ver mas detalle ' + url
		
		email = str(User.objects.get(id=request.user.id).email)

		url ="http://104.131.190.25/email/"

		params = {'asunto':asunto,'descripcion':cuerpo,'origen':'tasky@xiencias.org','destino':[email,'andyjo@xiencias.org','mayra@xiencias.org','alvarobencor@xiencias.org']}

		headers = {'Content-type': 'application/json', 'Accept': 'text/json'}

		r = requests.post(url, data=json.dumps(params), headers=headers)


		return render_to_response('ticket/movil.html',{'ticket':c},context_instance=RequestContext(request))
	

	else:
	
		form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
	documents = Document.objects.all()
	

    # Render list page with the documents and the form
	return render_to_response(
        'ticket/agregar_ticket_m.html',
        {'tipos':tipos,'documents': documents, 'form': form,'username':username,'grupo':grupo},
        context_instance=RequestContext(request)
    )


@login_required(login_url="/logeate")
def documentos(request,id_ticket):

	id =request.user.id

	ticket = Ticket.objects.get(id=id_ticket)
	username = request.user.username
	
	x=User.objects.get(username=username)
	grupo =x.groups.get()
	grupo= str(grupo)

	data = Values(grupo,username,id)

	documentos = Document.objects.filter(ticket=id_ticket)

	return render(request, 'ticket/documentos.html', {'users':data['users'],'ac':data['ac'],'oc':data['oc'],'tta':data['tta'],'documentos':documentos,'grupo':grupo,'username':username,'ticket':ticket})

@login_required(login_url="/logeate")
def document_event(request,id):

	idx= request.user.id

	evento = Evento.objects.get(id=id)
	username = request.user.username

	
	documentosp = Document.objects.filter(ticket=evento.evento_id)
	
	
	noti = Notificaciones.objects.all().order_by('-id')[:8]
	x=User.objects.get(username=username)
	grupo =x.groups.get()
	grupo= str(grupo)

	documentos = Document_Event.objects.filter(evento_id=id)

	print documentos

	documentosall = Document_Event.objects.filter(evento__evento=evento.evento_id)

	data = Values(grupo,username,idx)

	return render(request, 'ticket/documentos.html', {'t':data['t'],'users':data['users'],'tta':data['tta'],'ac':data['ac'],'oc':data['oc'],'documentosp':documentosp,'documentosall':documentosall,'evento':evento,'documentos':documentos,'grupo':grupo,'username':username})


@login_required(login_url="/logeate")
def agregar_ticket_m(request):

	if request.user.is_authenticated():

		id =request.user.id
		tipos=Tipo.objects.all()
		username = request.user.username

		x=User.objects.get(username=username)
		grupo =x.groups.get()
		grupo= str(grupo)

		clientes= Empresa.objects.all()

		data = Values(grupo,username,id)

		return render(request, 'ticket/agregar_ticket_m.html', {'users':data['users'],'clientes':clientes,'tta':data['tta'],'t':data['t'],'ac':data['ac'],'oc':data['oc'],'username':username,'grupo':grupo})

	else:

		return HttpResponseRedirect("/logeate")



@login_required(login_url="/logeate")
def ttcerrados(request):

	
	username = request.user.username
	
	id = request.user.id
	x=User.objects.get(pk=id)
	grupo =x.groups.get()
	grupo=str(grupo)

	if grupo=='Soporte' :

		ticket = Ticket.objects.all().values('fecha_fin','estado__name','asunto','cliente__first_name','soporte_actual','id','asunto','fecha_inicio').order_by('-fecha_fin')

		






	paginator = Paginator(ticket, 20) # Show 25 contacts per page

	page = request.GET.get('page')

	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
    # If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)


	sa = request.user.username

	data = Values(grupo,sa,id)

	
	return render(request, 'ticket/ttcerrados.html', {'ticket':ticket,'users':data['users'],'tta':data['tta'],'t':data['t'],'ac':data['ac'],'oc':data['oc'],'username':sa,'grupo':grupo,'contacts':contacts})




#Tutos

def pantallas(request):

	return render(request,'ticket/pantallas.html', {})

@login_required(login_url="/logeate")
def help(request):

	return render(request,'ticket/pantallas.html', {})


#Inv

@login_required(login_url="/logeate")
def eliminar_telefono(request,id):

	
	
	telefono = Telefono.objects.get(id=id).delete()

	return HttpResponseRedirect("/telefono/"+str(request.user.id))

@login_required(login_url="/logeate")
def email(request):

	

	#send_mail('MailGun works great!', 'It really really does.', 'tasky@xiencias.org', ['joelunmsm@gmail.com'], fail_silently=False)
	
	
	

	

	return render(request,'ticket/pantallas.html', {})

