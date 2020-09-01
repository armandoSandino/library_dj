from django.db import models
# Managers
from .managers import AutorManager

class Autor(models.Model):
    nombre = models.CharField(
        'Nombre',
        max_length=50,
        blank=False
    )
    apellidos = models.CharField(
        'Apellidos',
        max_length=50,
        blank=False
    )
    nacionalidad = models.CharField(
        'Nacionalidad',
        max_length=30,
        blank=False
    )
    # Entero positivo, PositiveIntegerField
    edad = models.PositiveIntegerField('Edad',blank=False)

    # Le indicara a nuestro modelo que trabaje con este administrador
    objects = AutorManager()

    def __str__(self):
        return self.nombre + ' ' + self.apellidos