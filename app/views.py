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

#mis vistas

def index(request):
	banners = Banner.objects.all()

	return render(request, "index.html", {"banners":banners})

def contacto(request):
	return render(request, "contacto.html", {})

def negocios(request):
	return render(request, "negocios.html", {})

def nosotros(request):
	return render(request, "nosotros.html", {})
