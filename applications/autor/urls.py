from django.contrib import admin
from django.urls import path 

from . import views

# Variable con la que invocaremos rutas desde codigo utilizando 'reverse_lazy'
app_name = 'autor_app'

urlpatterns = [
    path('autores/', views.ListAutores.as_view(), name='list-autores')
]
