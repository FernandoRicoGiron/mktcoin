from django.db import models
from django.utils import timezone
import datetime
from django.db import migrations
from django.dispatch import receiver
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
import json

# Create your models here.


class Banner(models.Model):
	banner = models.ImageField(upload_to='banners')
	titulo = models.CharField(max_length= 250, null=True, blank=True)
	subtitulo =  models.CharField(max_length=250, null=True, blank=True)

	def __str__(self):
		return "Banner " + str(self.id)


class Categoria(models.Model):
	nombre = models.CharField(null=True, blank= True, max_length=200)

	def __str__(self):
		return self.nombre

class Imagen(models.Model):
	imagen = models.ImageField(upload_to='registro_empresa')

	class Meta:
		verbose_name = "Imagen"
		verbose_name_plural = "Imagenes"
		
	def __str__(self):
		return "Imagen " + str(self.id)

class Municipio(models.Model):
	municipio = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Estado"
		verbose_name_plural = "Estados"
		
	def __str__(self):
		return self.municipio

class Estado(models.Model):
	estado = models.CharField(max_length=100)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Pais"
		verbose_name_plural = "Paises"
		
	def __str__(self):
		return self.estado

class Ubicacion(models.Model):
	latitud = models.CharField(max_length=100)
	longitud = models.CharField(max_length=100)
	#pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Ubicacion"
		verbose_name_plural = "Ubicaciones"
		
	def __str__(self):
		return "Ubicacion " + str(self.id)	


class Negocio(models.Model):
	validado = models.BooleanField(default=False)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	nombreTitular = models.CharField(max_length=100)
	fechaNacimiento =  models.DateField()
	numeroTelefonotitular = models.CharField(null=True, blank=True, max_length=20)
	direccionTitular = models.CharField(null=True,blank=True,max_length=100)
	correo = models.CharField(max_length=100)
	nombreEmpresa = models.CharField(null=True, blank= True, max_length=100)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, blank=True, null=True)
	descripcion =  models. TextField(null=True, blank= True)
	#estado = models.CharField(null=True, blank= True, max_length=50)
	#municipio = models.CharField(null=True, blank= True, max_length=50)
	direccionEmpresa = models.CharField(null=True, blank= True,max_length=100)
	numTel = models.CharField(null=True, blank= True, max_length=20)
	quieninvito = models.CharField(null=True, blank= True, max_length=50)
	loginmkt = models.CharField(null=True, blank= True, max_length=50)
	porcentaje = models.IntegerField(null=True, blank= True, default=0)
	facebook = models.URLField()
	instagram = models.URLField()
	youtube = models.URLField()
	twitter = models.URLField()
	whatsapp = models.URLField()
	sitioweb = models.URLField()
	comentarios =  models.TextField(null=True, blank= True)
	imgPortada = models.ImageField()
	imagenes = models.ManyToManyField(Imagen)

class Testimonios(models.Model):
	imagen = models.ImageField(upload_to='testimonios')
	descripcion = models.TextField()

