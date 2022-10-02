from hashlib import new
from django.db import models

# Create your models here.


class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha = models.DateTimeField(null=True)
