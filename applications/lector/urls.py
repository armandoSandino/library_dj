from django.contrib import admin
from django.urls import path

from .views import (
    RegistrarPrestamo, 
    AgregarPrestamo, 
    Notifications,
    AgregarPrestamoMultiple
)

# Variable con la que invocaremos rutas desde codigo utilizando 'reverse_lazy'
app_name = 'lector_app'

urlpatterns = [
    path(
        'prestamo/agregar/',
        AgregarPrestamo.as_view(),
        name='agregar-prestamo'
    ),
    path(
        'prestamo/agregar/multiple/',
        AgregarPrestamoMultiple.as_view(),
        name='agregar-prestamo-multiple'
    ),
    path(
        'success/',
        Notifications.as_view(),
        name='success-operation'
    )
]