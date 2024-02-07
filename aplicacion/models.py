from django.db import models


class Ingreso(models.Model):
    ingreso= models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

class Gasto(models.Model):
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10,decimal_places=0)
    fecha = models.CharField(max_length=100)

class Objetivo(models.Model):
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)