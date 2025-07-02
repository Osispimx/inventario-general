from django.db import models

class baseItem(models.Model):
    nombre = models.CharField(max_length=50)
    en_servicio= models.BooleanField()
    detalles= models.CharField(max_length=250)
    class Meta:
         abstract=True
    def __str__(self):
         return self.nombre

class inventarioTel(models.Model):

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

class equipoPcCom(baseItem):
    modelo= models.CharField(max_length=25)
    departamento=models.CharField(max_length=15)
    serie=models.CharField(max_length=50)

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
    cantidad=models.IntegerField()#si hay
