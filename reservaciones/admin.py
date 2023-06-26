from django.contrib import admin

from perfil.models import Profesor
from reservaciones.models import ReservacionesLab, ReservacionesMaq

# Register your models here.

admin.site.register(ReservacionesLab)
admin.site.register(ReservacionesMaq)
