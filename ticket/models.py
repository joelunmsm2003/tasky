from django.db import models
from django.contrib.auth.models import Group, User
from django import forms


class Empresa(models.Model):

 	id = models.AutoField(max_length=100,primary_key=True)
 	name = models.CharField(max_length=128)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Chat(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100,blank=True)
    chat= models.CharField(max_length=100,blank=True)
    fecha = models.DateTimeField(null=True,blank=True)
    

    def __str__(self):              # __unicode__ on Python 2
		return self.chat



class Usuarios(User):

    usuario_id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100,blank=True)
    ciudad = models.CharField(max_length=100,blank=True)
    empresa = models.ForeignKey(Empresa)
    version = models.CharField(max_length=100,blank=True)

    def __str__(self):              # __unicode__ on Python 2
		return self.usuario_id,self.empresa


class Admin:
	
	list_display=('empresa')


class Telefono(models.Model):

	id = models.AutoField(max_length=100,primary_key=True)
	user = models.ForeignKey(User)
	telefono = models.CharField(max_length=1000,blank=True)
	tipo = models.CharField(max_length=1000,blank=True)


	def __str__(self):              # __unicode__ on Python 2
		return self.telefono



    

class FormTicket(forms.Form):

    cc_myself = forms.BooleanField(required=False)


class Tipo(models.Model):

	name = models.CharField(max_length=100,blank=True)
	fecha_inicio = models.DateTimeField(null=True,blank=True)
	comentario = models.CharField(max_length=100,blank=True)
	comentario1 = models.CharField(max_length=100,blank=True)
	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Estado(models.Model):

	name = models.CharField(max_length=100,blank=True)
	fecha_inicio = models.DateTimeField(null=True,blank=True)
	comentario = models.CharField(max_length=100,blank=True)
	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Ticket(models.Model):

	id = models.AutoField(max_length=100,primary_key=True)
	cliente = models.ForeignKey(User)
	asunto = models.CharField(max_length=100,blank=True)
	tipo = models.ForeignKey(Tipo)
	soporte_actual = models.CharField(max_length=100,blank=True)
	empresa = models.ForeignKey(Empresa)
	descripcion = models.TextField(blank=True)
	fecha_inicio = models.DateTimeField()
	fecha_fin = models.DateTimeField(null=True,blank=True)
	estado = models.ForeignKey(Estado)
	cancha = models.CharField(max_length=100,blank=True)
	
	comentario = models.CharField(max_length=100,blank=True)
	def __str__(self):              # __unicode__ on Python 2
		return self.asunto


class Soporte(models.Model):

	id = models.AutoField(max_length=100,primary_key=True)
	ticket = models.ForeignKey(Ticket)
	titulo = models.CharField(max_length=1000,blank=True)
	fecha_inicio = models.DateTimeField()
	fecha_fin= models.DateTimeField(null=True,blank=True)
	soporte = models.ForeignKey(User,)
	
	comentario = models.CharField(max_length=100,blank=True)
	

	def __str__(self):              # __unicode__ on Python 2
		return self.titulo

class Evento(models.Model):

	id = models.AutoField(max_length=100,primary_key=True)
	evento = models.ForeignKey(Ticket)
	user = models.ForeignKey(User,)
	name = models.TextField(max_length=1000,blank=True)
	fecha_inicio = models.DateTimeField(null=True,blank=True)
	comentario = models.CharField(max_length=100,blank=True)

	def __str__(self):              # __unicode__ on Python 2
		return self.name


class Notificaciones(models.Model):

	id = models.AutoField(max_length=100,primary_key=True)
	ticket = models.ForeignKey(Ticket)
	tipo =models.CharField(max_length=100,blank=True)
	name = models.CharField(max_length=100,blank=True)
	fecha_inicio = models.DateTimeField(null=True,blank=True)
	comentario = models.CharField(max_length=100,blank=True)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Document_Event(models.Model):

	id = models.AutoField(max_length=100,primary_key=True)
	docfile = models.FileField(upload_to='files')
	evento = models.ForeignKey(Evento)
	user = models.ForeignKey(User,)
	asunto = models.CharField(max_length=100,blank=True)
	fecha_inicio = models.DateTimeField(null=True,blank=True)

class Document(models.Model):

	id = models.AutoField(max_length=100,primary_key=True)
	docfile = models.FileField(upload_to='files')
	ticket = models.ForeignKey(Ticket)
	detalle = models.CharField(max_length=100,blank=True)
	user = models.ForeignKey(User,)
	asunto = models.CharField(max_length=100,blank=True)
	asunto1 = models.CharField(max_length=100,blank=True)
	fecha_inicio = models.DateTimeField(null=True,blank=True)

class Archivo(models.Model):
	
	id = models.AutoField(max_length=100,primary_key=True)
	ticket = models.ForeignKey(Ticket)
	docfile = models.FileField(upload_to='/')
	asunto =models.CharField(max_length=100,blank=True)
	asunto =models.CharField(max_length=100,blank=True)
	user = models.ForeignKey(User,)
	fecha_inicio = models.DateTimeField(null=True,blank=True)















