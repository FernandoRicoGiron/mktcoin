from django.shortcuts import render
from django.db.models import Q
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
from .forms import *
from django.views.generic import FormView, ListView, UpdateView
import json
import smtplib
import sweetify
import datetime
from django.contrib.gis.geos import *
from django.contrib.gis.measure import Distance

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
	testimonios = Testimonio.objects.all()
	negocios = Negocio.objects.all()
	negocio = []
	negociocuatro = []
	for i in negocios[::-1]:
		negociosdos = [i]
		negocio = negocio + negociosdos

	for j in negocio [:6]:
		negociotres = [j]
		negociocuatro =  negociocuatro + negociotres

	resultado =  negociocuatro
	


	return render(request, "index.html", {"resultado":resultado,"negocios":negocios,"banners":banners, "testimonios":testimonios})

def contacto(request):
	return render(request, "contacto.html", {})

def filtro(request):
	categoria = request.POST.get("categoria")
	nombre = request.POST.get("negocio")
	pais = request.POST.get("pais")
	estado = request.POST.get("estado")
	municipio = request.POST.get("municipio")
	print(categoria + " " + nombre + " " + pais + " " + estado + " " + municipio)
	if pais != "" and estado != "" and categoria != "" and municipio != "":
		negocios = Negocio.objects.filter(validado=True, nombreEmpresa__icontains=nombre, pais__id=pais, estado__id=estado, municipio=municipio, categoria__id=categoria).exclude(ubicacion__isnull=True)
	elif pais != "" and estado != "" and categoria != "":
		negocios = Negocio.objects.filter(validado=True, nombreEmpresa__icontains=nombre, pais__id=pais, estado__id=estado, categoria__id=categoria).exclude(ubicacion__isnull=True)
	elif pais != "" and estado != "":
		negocios = Negocio.objects.filter(validado=True, nombreEmpresa__icontains=nombre, pais__id=pais, estado__id=estado).exclude(ubicacion__isnull=True)
	elif categoria != "":
		negocios = Negocio.objects.filter(validado=True, nombreEmpresa__icontains=nombre, categoria__id=categoria).exclude(ubicacion__isnull=True)
	else:
		negocios = Negocio.objects.filter(validado=True, nombreEmpresa__icontains=nombre).exclude(ubicacion__isnull=True)
	negocios2 = Negocio.objects.filter(validado=True)
	paiseslist = []
	for negocio in negocios2:
		paiseslist.append(negocio.pais.pais)
	paises = Pais.objects.filter(pais__in=paiseslist)
	estados = Estado.objects.all()
	categorias = Categoria.objects.all()

	return render(request, "negocios.html", {"negocios":negocios, "paises":paises, "estados":estados, "categorias":categorias})

def filmunicipio(request):
	municipio =  request.POST.get("municipio")
	negocios = Negocio.objects.filter(Q(validado=True) and ~Q(ubicacion=None) and Q(municipio__icontains=municipio))
	return render(request,"negocios.html",{"negocios":negocios, "municipio":municipio})

def negocios(request):
	negocios = Negocio.objects.filter(validado=True)
	paiseslist = []
	for negocio in negocios:
		paiseslist.append(negocio.pais.pais)
	paises = Pais.objects.filter(pais__in=paiseslist)
	estados = Estado.objects.all()
	categorias = Categoria.objects.all()

	#return render(request, "negocios.html", {"negocios":negocios, "paises":paises, "estados":estados})

	return render(request, "negocios.html", {"negocios":negocios, "paises":paises, "estados":estados, "categorias":categorias})





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

@csrf_exempt
def changepaises(request):
	# print(request.POST.get("pais"))
	estados = Estado.objects.filter(pais__id=request.POST.get("id"))
	data = {}
	for estado in estados:
		data[estado.id] = estado.estado
	print(data)
	return JsonResponse(data)

@login_required
def registronegocio(request):
	categorias = Categoria.objects.all()
	#ubicacion = Ubicacion.objects.all()
	negocios2 = Negocio.objects.filter(validado=True)
	paiseslist = []
	for negocio in negocios2:
		paiseslist.append(negocio.pais.pais)
	paises = Pais.objects.filter(pais__in=paiseslist)
	form = NegocioForm()

	return render(request, "registronegocio.html", {"categorias":categorias, "form":form, "paises":paises})

def altanegocio(request):
	usuario = request.user
	categoria =  Categoria.objects.get(id=request.POST.get("categoria"))
	pais =  Pais.objects.get(id=request.POST.get("pais"))
	estado =  Estado.objects.get(id=request.POST.get("estado"))
	
	negocio = Negocio.objects.create(usuario=usuario,
		ubicacion = request.POST["ubicacion"],
		nombreTitular = request.POST.get("nombreTitular"),
		fechaNacimiento= request.POST.get("fechaNacimiento"),
		numeroTelefonotitular =request.POST.get("numeroTelefonotitular"),
		direccionTitular=request.POST.get("direccionTitular"),
		correo= request.POST.get("correo"),
		nombreEmpresa= request.POST.get("nombreEmpresa"),
		categoria = categoria,
		pais= pais,
		estado=estado,
		municipio=request.POST.get("municipio"),
		descripcion =request.POST.get("descripcion"),
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
	negocio.imgPortada = request.FILES["imagenp"]

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
	
def descripcionnegocio(request, id):
	negocio = Negocio.objects.get(id=id)
	paises = Pais.objects.all()
	return render(request, "descripcionnegocio.html",{"negocio":negocio, "paises":paises})

def modificar(request):
	user = request.user
	paises = Pais.objects.all()
	categorias = Categoria.objects.all()
	
	form = NegocioForm()
	if Negocio.objects.filter(usuario=user).exists():
		negocio = Negocio.objects.get(usuario=user)
		return render(request, "modificarnegocio.html",{"form":form,"negocio":negocio,"paises":paises,"categorias":categorias})
	else:
		sweetify.success(request, '!Opps!', text="Registra tu negocio porfavor", persistent=':)')
		return redirect("/registronegocio/")


def modificarnegocio(request):	
	user = request.user
	negocio = Negocio.objects.get(usuario=user)
	categoria =  Categoria.objects.get(id=request.POST.get("categoria"))
	pais =  Pais.objects.get(id=request.POST.get("pais"))
	estado =  Estado.objects.get(id=request.POST.get("estado"))

	if request.POST["ubicacion"]:
		negocio.ubicacion = request.POST["ubicacion"],
	negocio.nombreTitular = request.POST.get("nombreTitular"),
	negocio.fechaNacimiento= request.POST.get("fechaNacimiento"),
	negocio.numeroTelefonotitular =request.POST.get("numeroTelefonotitular"),
	negocio.direccionTitular=request.POST.get("direccionTitular"),
	negocio.correo= request.POST.get("correo"),
	negocio.nombreEmpresa= request.POST.get("nombreEmpresa"),
	negocio.categoria = categoria,
	negocio.pais= pais,
	negocio.estado=estado,
	negocio.municipio=request.POST.get("municipio"),
	negocio.descripcion =request.POST.get("descripcion"),
	negocio.direccionEmpresa=request.POST.get("direccionEmpresa"),
	negocio.numTel=request.POST.get("numTel"),
	negocio.quieninvito=request.POST.get("quieninvito"),
	negocio.loginmkt=request.POST.get("loginmkt"),
	negocio.porcentaje=request.POST.get("porcentaje"),
	negocio.facebook=request.POST.get("facebook"),
	negocio.instagram =request.POST.get("instagram"),
	negocio.youtube= request.POST.get("youtube"),
	negocio.twitter=request.POST.get("twitter"),
	negocio.whatsapp=request.POST.get("whatsapp"),
	negocio.sitioweb=request.POST.get("sitioweb"),
	negocio.comentarios= request.POST.get("comentarios"),

	negocio.imgPortada = request.FILES["imagenp"]

	lista = request.FILES.getlist("imagen")
	for f in lista:
		image = Imagen.objects.create(imagen=f)
		negocio.imagenes.add(image) 

	negocio.save()

	sweetify.success(request, 'Gracias!', text="Ha sido modificado correctamente", persistent=':)')
	return HttpResponseRedirect('/')
