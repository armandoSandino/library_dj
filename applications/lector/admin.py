from django.contrib import admin
# Models
from .models import Lector, Prestamo

class LectorAdmin(admin.ModelAdmin):
    # lista de campos a mostrar en el administrador
    list_display = (
        'id',
        'nombres',
        'apellidos',
        'full_name',
        'nacionalidad',
        'edad'
    )
    # agregar valor al campo que no existe en mi modelo 'full_name'
    def full_name(self, obj):

        return obj.nombres + ' '+ obj.apellidos 

    # agregar/hablitar filtros para los campos
    list_filter = (
        'nombres',
        'apellidos',
        'nacionalidad',
        'edad'
    )
    # agregar/habilitar buscador, puede especificar los campos por los que buscar
    search_fields = (
        'nombres',
        'nacionalidad'
    )
    ordering = ('edad',)


admin.site.register(Lector,LectorAdmin)

class PrestamoAdmin(admin.ModelAdmin):
    # lista de campos a mostrar en el administrador
    list_display = (
        'id',
        'lector',
        'libro',
        'fecha_prestamo',
        'fecha_devolucion',
        'devuelto'
    )
    # agregar/hablitar filtros para los campos
    list_filter = (
        'fecha_prestamo',
        'devuelto'
    )
    # agregar/habilitar buscador, puede especificar los campos por los que buscar
    search_fields = (
        'libro',
        'fecha_prestamo'   
    )

admin.site.register(Prestamo, PrestamoAdmin)