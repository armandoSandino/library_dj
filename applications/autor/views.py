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
        # queryset = super(ListAutores, self).get_queryset()
        # queryset = queryset
        return Autor.objects.all()

    
