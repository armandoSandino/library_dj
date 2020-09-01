from django.contrib import admin
from django.urls import path
# Views
from . import views

# Variable con la que invocaremos rutas desde codigo utilizando 'reverse_lazy'
app_name = 'libro_app'

urlpatterns = [
    path('libros/', views.ListaLibros.as_view(), name = 'list-book' )
]