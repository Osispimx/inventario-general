from django.db import models

from django.utils import timezone
# Create your models here.

class baseItem(models.Model):
    propietario = models.CharField(max_length=50)
    en_servicio= models.BooleanField()
    detalles= models.TextField()
    fecha=models.DateField(default=timezone.now)
    class Meta:
         abstract=True
    def __str__(self):
         return self.nombre
class equipoPcCom(baseItem):
    marca= models.CharField(max_length=25)
    departamento=models.CharField(max_length=15)
    imei=models.CharField(max_length=50)
    contrasena_ingreso= models.CharField(max_length=100)
