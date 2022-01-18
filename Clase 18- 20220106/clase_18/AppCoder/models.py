from unittest.util import _MAX_LENGTH
from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, BooleanField, DateField, EmailField
# Create your models here.

class curso(Model):
    nombre= CharField(max_length=40)
    camada= IntegerField()

class estudiante(Model):
    nombre= CharField(max_length=30)
    apellido= CharField(max_length=30)
    email= EmailField()

class profesor(Model):
    nombre= CharField(max_length=30)
    apellido= CharField(max_length=30)
    email= EmailField()
    profesion = CharField(max_length=30)

class entregablo(Model):
    nombre= CharField(max_length=30)
    fecha_entrega= DateField()
    entregado= BooleanField()