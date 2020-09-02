from django.contrib import admin
from .models import Persona, Empleado

class PersonaAdmin(admin.ModelAdmin):

    # Campos a mostrar
    list_display = (
        'id',
        'full_name',
        'pais',
        'pasaporte',
        'edad',
        'apelativo'
    )
    search_fields = (
        'full_name',
        'edad'
    )
    # Habilitar filtros laterales en el administrador
    list_filter = (
        'pais',
        'edad'
    )

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Empleado)