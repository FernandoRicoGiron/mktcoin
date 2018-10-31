from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from mapwidgets.widgets import GooglePointFieldWidget

CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 13),
        ("mapCenterLocation", [16.753043887702606, -93.12201404296877]),
    ),
    "GOOGLE_MAP_API_KEY": "AIzaSyAJmeDzN7crTR_s0JzVby6WQlWxuRitDHE",
}

class Negocios(admin.ModelAdmin):
	formfield_overrides = {
		pos.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
	}
	list_display = ["id","nombreEmpresa"]
	list_display_links = ["id","nombreEmpresa"]
	search_fields = ['nombreEmpresa']
	 
	class Meta:
		model = Negocio

admin.site.register(Banner)
admin.site.register(Categoria)
admin.site.register(Imagen)
admin.site.register(Negocio, Negocios)
admin.site.register(Estado)
admin.site.register(Pais)
admin.site.register(Testimonio)