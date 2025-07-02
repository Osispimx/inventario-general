from django import forms
from .models import inventarioTel

class inventarioform(forms.ModelForm):
    class Meta:
        model = inventarioTel
        fields =['telefono', 'marca', 'email', 'en_servicio', 'detalles', 'contrasena_ingreso', 'propietario', 'imei']
