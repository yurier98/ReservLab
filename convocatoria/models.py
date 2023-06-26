from django.db import models

from perfil.models import Estudiante


# Create your models here.

class Convocatoria(models.Model):
    ESTADO = (
        ('b', 'borrador'),
        ('p', 'publicado'),
        ('e', 'eliminado'),
    )
    tiitulo = models.CharField(max_length=255)
    contenido = models.CharField(max_length=252)
    estado = models.CharField(max_length=1, choices=ESTADO)
    autor = models.CharField(max_length=100)
    creado = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pelucaso')


class Inscripciones(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    convocatoria = models.ForeignKey(Convocatoria, on_delete=models.CASCADE)
