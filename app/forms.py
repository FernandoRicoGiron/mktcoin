from django import forms
from .models import *
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 13),
        ("mapCenterLocation", [16.753043887702606, -93.12201404296877]),
    ),
    "GOOGLE_MAP_API_KEY": "AIzaSyAJmeDzN7crTR_s0JzVby6WQlWxuRitDHE",
}

class NegocioForm(forms.ModelForm):

    class Meta:
        model = Negocio
        fields = ("ubicacion",)
        widgets = {
            'ubicacion': GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS),
            # 'city_hall': GoogleStaticOverlayMapWidget,
        }