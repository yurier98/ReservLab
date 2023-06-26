from django.contrib import admin

from laboratorio.models import Laboratorio, Maquina, Material


# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cant_maq', 'capacidad', 'tecnico','ubicacion')
    list_filter = ['ubicacion','tecnico']
    search_fields = ['nombre']


admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Maquina)
admin.site.register(Material)
