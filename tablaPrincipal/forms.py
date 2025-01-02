from django import forms
from .models import inventario

class inventarioform(forms.ModelForm):
    class Meta:
        model = inventario
        fields =['telefono', 'marca', 'email', 'en_servicio', 'detalles', 'contrasena_ingreso', 'propietario', 'imei']
