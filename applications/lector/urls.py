from django.contrib import admin
from django.urls import path

from .views import RegistrarPrestamo

urlpatterns = [
    path(
        'prestamo/agregar/',
        RegistrarPrestamo.as_view(),
        name='agregar-prestamo'
    )
]