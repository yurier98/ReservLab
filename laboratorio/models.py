from django.db import models

from perfil.models import Tecnico, Profesor


# Create your models here.


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50)
    cant_maq = models.IntegerField('Cantidad de maquinas')
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=50)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Material(models.Model):
    TIPO = (
        ('A', 'Audio'),
        ('V', 'Video'),
        ('D', 'Documento'),
        ('P', 'Pdf'),
        ('O', 'Otro'),
    )
    nombre = models.CharField(max_length=15)
    tipo = models.CharField(choices=TIPO, max_length=1)
    autor = models.CharField(max_length=50)
    descipcion = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    idioma = models.CharField(max_length=15)
    fecha_publicacion = models.DateTimeField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)


class Maquina(models.Model):
    ESTADO = (
        ('D', 'Disponible'),
        ('O', 'Ocupado'),
        ('R', 'Rota'),
    )

    solapin = models.CharField(max_length=50)
    nombre = models.CharField(max_length=20)
    inventario = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=ESTADO, default='D')
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
