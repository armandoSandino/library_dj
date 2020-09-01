from django.shortcuts import render
# Generic views
from django.views.generic import ListView
# Models
from .models import Categoria, Libro

class ListaLibros(ListView):

    template_name = 'libro/lista.html'
    context_object_name = 'listaLibro'
    

    def get_context_data(self, **kwargs):
        context = super(ListaLibros, self).get_context_data(**kwargs)
        context['titulo'] = 'Todos los libros'
        return context

    def get_queryset(self):
        termino  = self.request.GET.get('term', '')
        return Libro.objects.buscar_libro(termino)
