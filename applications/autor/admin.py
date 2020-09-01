from django.contrib import admin

from .models import Autor



class AutorAdmin(admin.ModelAdmin):
    '''Admin View for AutorAdmin '''

    list_display = (
        'id',
        'nombre',
        'apellidos',
        'full_name',
        'nacionalidad',
        'edad'
    )
    # agregar valor al campo que no existe en mi modelo 'full_name'
    def full_name(self, obj ):
        return obj.nombre + ' ' + obj.apellidos

    # agregar/hablitar filtros para los campos
    list_filter = ('edad','nacionalidad')
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # agregar/habilitar buscador, puede especificar los campos por los que buscar
    search_fields = ('nombre','apellidos','nacionalidad')
    # date_hierarchy = ''
    ordering = ('nombre',)


admin.site.register(Autor, AutorAdmin)


