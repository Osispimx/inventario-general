from django.db import models

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
    
class equipoPcCom():
    nombre = models.CharField(max_length=50)
    modelo= models.CharField(max_length=25)
    en_servicio=models.BooleanField()
    detalles=models.CharField(max_length=100)
    departamento=models.CharField(max_length=15)
    serie=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class operaciones():
    nombre = models.CharField(max_length=50)
    en_servicio=models.BooleanField()
    detalles=models.CharField(max_length=100)
    cantidad=models.IntegerField()
    serie=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class herramienta():
    nombre = models.CharField(max_length=50)
    en_servicio=models.BooleanField()
    cantidad=models.IntegerField()
    detalles=models.CharField(max_length=100)
def __str__(self):
        return self.nombre

class papeleria():
    nombre = models.CharField(max_length=50)
    cantidad=models.IntegerField()
    detalles=models.CharField(max_length=100)
def __str__(self):
        return self.nombre

class vehiculos():
    nombre = models.CharField(max_length=50)
    en_servicio=models.BooleanField()
    detalles=models.CharField(max_length=100)
def __str__(self):
        return self.nombre
class uniformes():
    nombre = models.CharField(max_length=50)
    cantidad=models.IntegerField()
    detalles=models.CharField(max_length=200)
def __str__(self):
        return self.nombre
class muebles():
    nombre = models.CharField(max_length=50)
    en_servicio=models.BooleanField()
    detalles=models.CharField(max_length=200)
def __str__(self):
        return self.nombre

def otro():
    nombre = models.CharField(max_length=50)
    en_servicio=models.BooleanField()
    cantidad=models.IntegerField()#si hay
    detalles=models.CharField(max_length=200)
def __str__(self):
        return self.nombre
