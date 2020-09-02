from django.db import models
# Managers
from .managers import AutorManager

class Persona(models.Model):
    nombres = models.CharField(
        'Nombres',
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
        max_length=20,
        blank=False
    )
    # Entero positivo, PositiveIntegerField
    edad = models.PositiveIntegerField('Edad', blank=False, default=0)

    class Meta:
        # Le indicara al ORM de Django que este modelo sera una clase Abstracta de la cual extenderan otros modelos
        # Por lo cual podemos indicarle que no se cree en la base de datos
        abstract = True

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

class Autor(Persona):

    class Meta:
        verbose_name = 'El Autor'
        verbose_name_plural = 'Los autores'

    # Le indicara a nuestro modelo que trabaje con este administrador
    objects = AutorManager()

