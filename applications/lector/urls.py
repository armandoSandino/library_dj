from django.contrib import admin
from django.urls import path

from .views import RegistrarPrestamo, AgregarPrestamo

urlpatterns = [
    path(
        'prestamo/agregar/',
        AgregarPrestamo.as_view(),
        name='agregar-prestamo'
    )
]