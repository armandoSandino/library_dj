from django.contrib import admin
# Models
from .models import Categoria, Libro

class CategoriaAdmin(admin.ModelAdmin):
    # lista de campos a mostrar en el administrador
    list_display= (
        'id',
        'nombre'
    )
    # agregar/habilitar buscador, puede especificar los campos por los que buscar
    search_fields = ('nombre',)
    # agregar/hablitar filtros para los campos
    list_filter = ('nombre',)

    ordering = ('nombre',)

admin.site.register(Categoria, CategoriaAdmin)

class LibroAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'categoria',
        'titulo',
        'fecha',
        'visitas'
    )
    search_fields = ('titulo','visitas')
    list_filter = ('categoria','autores')
    # agregar filtro horizontal unicamente para las relaciones many to many
    filter_horizontal = ('autores',)



