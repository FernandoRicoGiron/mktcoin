from django.shortcuts import render

from django.shortcuts import render, render_to_response, redirect
from django.utils import timezone
from .models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.core import serializers
from django.contrib.auth.hashers import check_password
import json
import smtplib
import sweetify
import datetime

"""

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
"""
#mis vistas

def index(request):
	banners = Banner.objects.all()
	testimonios = Testimonios.objects.all()

	return render(request, "index.html", {"banners":banners, "testimonios":testimonios})

def contacto(request):
	return render(request, "contacto.html", {})


def negocios(request):
	negocios = Negocio.objects.filter(validado=True)
	paises = Pais.objects.all()
	estados = Estado.objects.all()
	return render(request, "negocios.html", {"negocios":negocios, "paises":paises, "estados":estados})



def nosotros(request):
	return render(request, "nosotros.html", {})


#SECCION DE CREACION DE USUARIOS
@csrf_exempt
def registrar(request):
	if request.method == 'POST':
		username = request.POST['usuario']
		password = request.POST['password']
		password_confirmation = request.POST['password_confirmation']

		if password != password_confirmation:
			sweetify.error(request, 'Oops!', text='¡Las contraseñas no coinciden!', persistent=':´(')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
			#return render(request, 'crearcuenta')

		user = User.objects.create_user(username=username, password=password)
		user.first_name= request.POST['nombre']
		user.last_name= request.POST['apellidos']
		user.email= request.POST['correo']
		user.save()

	sweetify.success(request, '¡Genial!', text='Se ha creado su usuario', persistent=':)')
	return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


  #SECCION DE INICIO Y CIERRE DE SESION

def iniciosesion(request):
	username = request.POST.get("usuario")
	password = request.POST.get("password")
	try: 
		username = authenticate(request, username=username, password=password)
		login(request,username)
		return redirect('/')
	except Exception as e:
		sweetify.error(request, 'Oops!', text='El usuario o la contraseña es incorrecto', persistent=':´(')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def cerrarsesion(request):
	logout(request)
	return HttpResponseRedirect("/")

@login_required
def registronegocio(request):
	categorias = Categoria.objects.all()
	#ubicacion = Ubicacion.objects.all()
	paises = Pais.objects.all()

	return render(request, "registronegocio.html", {"categorias":categorias,"paises":paises})

def altanegocio(request):
	usuario = request.user
	categoria =  Categoria.objects.get(id=request.POST.get("categoria"))
	pais =  Pais.objects.get(id=request.POST.get("pais"))

	negocio = Negocio.objects.create(usuario=usuario,
		nombreTitular = request.POST.get("nombreTitular"),
		fechaNacimiento= request.POST.get("fechaNacimiento"),
		numeroTelefonotitular =request.POST.get("numeroTelefonotitular"),
		direccionTitular=request.POST.get("direccionTitular"),
		correo= request.POST.get("correo"),
		nombreEmpresa= request.POST.get("nombreEmpresa"),
		categoria = categoria,
		pais= pais,
		descripcion =request.POST.get("descripcion"),
		estado = request.POST.get("estado"),
		municipio=request.POST.get("municipio"),
		direccionEmpresa=request.POST.get("direccionEmpresa"),
		numTel=request.POST.get("numTel"),
		quieninvito=request.POST.get("quieninvito"),
		loginmkt=request.POST.get("loginmkt"),
		porcentaje=request.POST.get("porcentaje"),
		facebook=request.POST.get("facebook"),
		instagram =request.POST.get("instagram"),
		youtube= request.POST.get("youtube"),
		twitter=request.POST.get("twitter"),
		whatsapp=request.POST.get("whatsapp"),
		sitioweb=request.POST.get("sitioweb"),
		comentarios= request.POST.get("comentarios"), 

		)

	
	lista = request.FILES.getlist("imagen")
	for f in lista:
		image = Imagen.objects.create(imagen=f)
		negocio.imagenes.add(image)
	negocio.save()

	sweetify.success(request, '¡Felicidades!', text='Se ha agregado con éxito', persistent=':)')
	return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def send_email(request):
    nombre = request.POST.get('nombre', '')
    mensaje = request.POST.get('mensaje', '')
    telefono = request.POST.get('telefono', '')
    correo = request.POST.get('correo', '')
    if nombre and mensaje and telefono and correo:
        try:
            sweetify.success(request, 'Gracias!', text="Su mensaje a sido enviado correctamente", persistent=':)')
            send_mail('Mensaje de ' + nombre, 'La empresa o el cliente ' + nombre + ' ha enviado la siguiente informacion: \n' + mensaje + '\n Su número de contacto es: ' + telefono, correo, ['wilderesc97@gmail.com'])
            
        except BadHeaderError:
            sweetify.error(request, 'Lo sentimos!', text='Revise sus datos', persistent=':´(')
            #return HttpResponse('No pudo enviarse')
        sweetify.success(request, 'Gracias!', text="Su mensaje a sido enviado correctamente", persistent=':)')
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Complete los campos de informacion')
	
def descripcionnegocio(request):
	
	return render(request, "descripcionnegocio.html",{})