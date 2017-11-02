from django.db import models
from ticket.models import *



# Create your models here.
class Equipos(models.Model):

	id = models.AutoField(primary_key=True)
	
	empresa = models.ForeignKey(Empresa)
	user = models.CharField(max_length=120)
	password = models.CharField(max_length=120)
	name = models.CharField(max_length=120)
	descripcion = models.CharField(max_length=120)
	ubicacion = models.CharField(max_length=120)
	ip = models.CharField(max_length=120,blank=True)

	def __str__(self):              # __unicode__ on Python 2
		return self.name


class Parametro(models.Model):
	
	id = models.AutoField(primary_key=True)
	ip = models.CharField(max_length=120)
	puerto_origen = models.CharField(max_length=120)
	puerto_final = models.CharField(max_length=120)
	equipo = models.ForeignKey(Equipos)
	tipo = models.CharField(max_length=120)
	servicio = models.CharField(max_length=120)
	user = models.CharField(max_length=120)
	password = models.CharField(max_length=120)


class Tipo(models.Model):
	
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Caracteristica(models.Model):
	
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120)

	def __str__(self):              # __unicode__ on Python 2
		return self.name

class Red(models.Model):
	
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=120)

	def __str__(self):              # __unicode__ on Python 2
		return self.name


class Rango(models.Model):
	
	id = models.AutoField(primary_key=True)
	red = models.ForeignKey(Red)
	empresa = models.ForeignKey(Empresa)
	tipo = models.ForeignKey(Tipo)
	caracteristica = models.ForeignKey(Caracteristica)
	ip = models.CharField(max_length=120)


