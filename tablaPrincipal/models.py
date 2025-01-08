from django.db import models

class inventario(models.Model):

    telefono = models.CharField(max_length=100)
    marca = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    en_servicio = models.BooleanField()
    detalles= models.TextField()
    contrasena_ingreso= models.CharField(max_length=100)
    propietario=models.TextField()
    imei=models.TextField()
    
    def __str__(self):
        return self.telefono
