from datetime import date

from django.shortcuts import render
# Generic views
from django.views.generic.edit import FormView
#Models
from .models import Prestamo
#Forms
from .forms import PrestamoForm

class RegistrarPrestamo(FormView):

    template_name = 'lector/agregar_prestamo.html'
    # Definir formulario a utilizar
    form_class = PrestamoForm
    # Ruta de direccionamiento
    success_url  = '.'

    # Validar datos del form
    def form_valid(self, form):
        # Crear el objeto a guardar
        # date.today(), retorna la fecha actual
        
        # Esta forma de registrar funciona tambien
        '''
        Prestamo.objects.create(
            lector= form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto = False
        )
        '''
        # Si existe un registro con la misma Data el 'save' los actualizara en cambio si no existe creara un nuevo registro
        prestamo = Prestamo(
            lector= form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto = False
        )
        prestamo.save()

        # Actualizar existencia, recuerde que puede sobreescribir la funccion 'save' desde los modelos
        '''
        libro = form.cleaned_data['libro']
        libro.stock = libro.stock-1
        libro.save()
        '''

        return super(RegistrarPrestamo, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super(RegistrarPrestamo, self).get_context_data(**kwargs)
        context['titulo'] = 'Agregar prestamo'
        return context
    
