from django.shortcuts import render
# Generic views
from django.views.generic import  ListView

# Models
from .models import Autor

class ListAutores(ListView):

    template_name = 'autor/lista.html'
    # model = Autor
    context_object_name = 'listAutores'
    success_url = '/'

    
    def get_context_data(self, **kwargs):
        context = super(ListAutores, self).get_context_data(**kwargs)
        context['titulo'] = 'Los autores'
        return context
    
    def get_queryset(self):
        # Si no tenemos un Manager podemos usar Autor.objects.all() para obtener la lista de datos
        # De otro modo intente con Manager
        
        return Autor.objects.listar_autores()

    
