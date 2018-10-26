from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(Banner)
admin.site.register(Categoria)
admin.site.register(Imagen)
admin.site.register(Negocio)
admin.site.register(Ubicacion)
admin.site.register(Pais)
admin.site.register(Estado)