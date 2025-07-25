from django.db import models
from django.utils import timezone

class baseItem(models.Model):
    nombre = models.CharField(max_length=50)
    en_servicio= models.BooleanField()
    detalles= models.TextField()
    fecha=models.DateField(default=timezone.now)
    class Meta:
         abstract=True
    def __str__(self):
         return self.nombre

class inventarioTel(baseItem):
    nombre=None
    telefono = models.CharField(max_length=100)
    marca = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    contrasena_ingreso= models.CharField(max_length=100)
    propietario=models.TextField()
    imei=models.TextField()
    def __str__(self):
        return self.telefono

class operaciones(baseItem):
    cantidad=models.IntegerField()
    serie=models.CharField(max_length=50)

class herramienta(baseItem):
    cantidad=models.IntegerField()

class papeleria():
    nombre = models.CharField(max_length=50)
    cantidad=models.IntegerField()
    detalles=models.CharField(max_length=100)

class vehiculos(baseItem):
     pass

class uniformes(baseItem):
    cantidad=models.IntegerField()

class muebles(baseItem):
    pass

def otro(baseItem):
    cantidad=models.IntegerField()#por si hay
