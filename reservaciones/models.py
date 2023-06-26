from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import DateTimeField

from laboratorio.models import Maquina, Laboratorio
from perfil.models import Estudiante, Profesor


# Create your models here


class ReservacionesMaq(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()


class ReservacionesLab(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
