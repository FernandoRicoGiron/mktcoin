from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index),
    path('contacto/', views.contacto),
    path('nosotros/', views.nosotros),
    path('negocios/filtro/', views.filtro),
    path('negocios/municipios/', views.filmunicipio),
    path('negocios/', views.negocios),
    path('registronegocio/', views.registronegocio),
    path('login/', views.iniciosesion, name='login'),
    path('cerrarsesion/', views.cerrarsesion),
    path('registrar/', views.registrar),
    path('altanegocio/', views.altanegocio),
    path('mensaje/', views.send_email),
    path('changepaises/', views.changepaises),
    re_path('negocios/(?P<id>\d+)/', views.descripcionnegocio),
    path('modificar/', views.modificar),
    path('modificarnegocio/', views.modificarnegocio),
   # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),

    ]