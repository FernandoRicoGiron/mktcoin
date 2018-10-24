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

	return render(request, "index.html", {"banners":banners})

def contacto(request):
	return render(request, "contacto.html", {})

def negocios(request):

	return render(request, "negocios.html", {})

def registronegocio(request):
	return render(request, "registronegocio.html", {})

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

"""
@csrf_exempt
def registrar(request):
	nombre =  request.POST.get("nombre")
	apellidos = request.POST.get("apellidos")
	correo = request.POST.get("correo")
	usuario = request.POST.get("usuario")
	password = request.POST.get("password")

	user = User.objects.filter(username=usuario).exists()
	if user == False:
		user = User.objects.create_user(first_name=nombre,
			last_name = apellidos,
			email = correo,
			username = usuario,
			password = password)
		user = authenticate(request, username=usuario, password=password)
		user.is_active = True
		current_site = get_current_site(request)
		mail_subject = 'Activacion de cuenta'
		message = render_to_string('acc_active_email.html',{
			'user':user,
			'domain':current_site.domain,
			'uid':urlsafe_base64_decode(force_bytes(user.pk)),
			'token':account_activation_token.make_token(user),
			})
		emaild = EmailMessage(mail_subject, message, to = [correo])
		emaild.send()
		sweetify.success(request, 'Gracias!', text='Valida Tu usuario en Tu Correo', persistent=':)')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
			#return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		
	else:
		sweetify.error(request, 'Oops!', text='¡Ese Nombre de Usuario ya Existe!', persistent=':´(')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
    	sweetify.success(request, 'Gracias!', text='Usuario Validado', persistent=':)')
    	return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
   """

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
