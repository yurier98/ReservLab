from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Perfil(AbstractUser):
    solapin = models.CharField(max_length=50)
    area = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Tecnico(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return self.perfil.first_name

class Estudiante(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    grupo = models.IntegerField()

    def __str__(self):
        return self.perfil.first_name

   

class Profesor(models.Model):
    CAT_DOCENTE = (
        ('Ins', 'Instruptor'),
        ('Asi', 'Asistente'),
        ('Tit', 'Titular'),
        ('Aux', 'Auxiliar'),
        ('Atd', 'ATD'),
    )
    cat_docente = models.CharField(choices=CAT_DOCENTE, max_length=3)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
