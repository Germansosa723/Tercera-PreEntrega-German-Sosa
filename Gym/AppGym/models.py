from django.db import models

# Create your models here.
class Entrenadores(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    email = models.EmailField()
    tipo_de_profesor = models.CharField(max_length=15)

class Inscriptos(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    email = models.EmailField()

class rutinas(models.Model):
    nombre = models.CharField(max_length=10)
    ejercicios = models.CharField(max_length=50)
