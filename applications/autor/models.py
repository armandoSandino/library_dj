from django.db import models

class Autor(models.Model):
    nombre = models.CharField(
        'Nombre',
        max_length=50,
        blank=False
    )
    apellidos = models.CharField(
        'Apellidos',
        max_length=50,
        blank=50
    )
    nacionalidad = models.CharField(
        'Nacionalidad',
        max_length=30,
        blank=False
    )
    # Entero positivo, PositiveIntegerField
    edad = models.PositiveIntegerField('Edad',blank=False)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos