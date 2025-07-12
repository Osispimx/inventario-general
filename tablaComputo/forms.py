from django import forms
from .models import equipoPcCom

class inventarioform(forms.ModelForm):
    class Meta:
        model = equipoPcCom
        fields =['marca', 'departamento', 'en_servicio', 'detalles', 'contrasena_ingreso', 'propietario', 'imei']
        widgets = {
            'detalles': forms.Textarea(attrs={'class': 'borde'}),
            'propietario': forms.Textarea(attrs={'class': 'borde'}),
            'imei': forms.Textarea(attrs={'class': 'borde'}),
            'contrasena_ingreso': forms.PasswordInput(attrs={'class': 'password borde', 'placeholder': 'Contraseña'}),
            }
