from django.db import models
from django.contrib.auth.models import User


class Ingreso(models.Model):
    ingreso= models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=0)

class Gasto(models.Model):
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10,decimal_places=0)
    fecha = models.CharField(max_length=100)

class Objetivo(models.Model):
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=0)

class Avatar(models.Model):
   imagen = models.ImageField(upload_to="avatares")
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   def __str__(self):
        return f"{self.user} {self.imagen}"   
    
#hay que cargarlo a la terminal