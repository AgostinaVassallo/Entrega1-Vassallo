from django.db import models

# Create your models here.
class Bts(models.Model):
    trayectoria=models.CharField(max_length=50)
    integrantes=models.CharField(max_length=50)
    edad=models.IntegerField() #averiguar si va un booleano
    carrera_musical=models.CharField(max_length=50)

class Coreasur(models.Model):
    historia=models.CharField(max_length=50)
    industria_cultural=models.CharField(max_length=50)
    soft_power=models.CharField(max_length=50)
    servicio_militar=models.CharField(max_length=50)

class Army(models.Model):
    resumen=models.CharField(max_length=50)
    poder_economico=models.CharField(max_length=50)
    influencia=models.CharField(max_length=50)