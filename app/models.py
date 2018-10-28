from django.db import models
from django.utils import timezone
import datetime
from django.db import migrations
from django.dispatch import receiver
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
import json
from django.contrib.gis.db import models as pos

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
		
	def __str__(self):
		return self.municipio

class Estado(models.Model):
	estado = models.CharField(max_length=100)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
		
	def __str__(self):
		return self.estado

class Pais(models.Model):
	pais = models.CharField(max_length=100)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Pais"
		verbose_name_plural = "Paises"
		
	def __str__(self):
		return self.pais


class Negocio(models.Model):
	validado = models.BooleanField(default=False)
	ubicacion = pos.PointField(null=False, blank=False, srid=4326, verbose_name="Location")
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	nombreTitular = models.CharField(max_length=100)
	fechaNacimiento =  models.DateField()
	numeroTelefonotitular = models.CharField(null=True, blank=True, max_length=20)
	direccionTitular = models.CharField(null=True,blank=True,max_length=100)
	correo = models.CharField(max_length=100)
	nombreEmpresa = models.CharField(null=True, blank= True, max_length=100)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=True, null=True)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, blank=True, null=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank=True, null=True)
	descripcion =  models. TextField(null=True, blank= True)
	direccionEmpresa = models.CharField(null=True, blank= True,max_length=100)
	numTel = models.CharField(null=True, blank= True, max_length=20)
	quieninvito = models.CharField(null=True, blank= True, max_length=50)
	loginmkt = models.CharField(null=True, blank= True, max_length=50)
	porcentaje = models.IntegerField(null=True, blank= True, default=0)
	whatsapp = models.CharField(max_length=50)
	facebook = models.URLField()
	instagram = models.URLField()
	youtube = models.URLField()
	twitter = models.URLField()
	sitioweb = models.URLField()
	comentarios =  models.TextField(null=True, blank= True)
	imgPortada = models.ImageField()
	imagenes = models.ManyToManyField(Imagen)

class Testimonio(models.Model):
	imagen = models.ImageField(upload_to='testimonios')
	descripcion = models.TextField()
		
	def __str__(self):
		return "Testimonio " + str(self.id)

