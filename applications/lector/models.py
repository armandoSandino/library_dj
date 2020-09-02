from django.db import models
# from local apps
from applications.libro.models import Libro


class Lector(models.Model):
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
    edad = models.PositiveIntegerField('Edad', blank=False, default=0)

    class Meta:
        verbose_name= "Lector"
        verbose_name_plural = "Lectores"

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

class Prestamo(models.Model):

    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE
    )
    libro= models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='libro_prestamo'
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(
        blank=True,
        null = True
    )
    devuelto = models.BooleanField()

    def __str__(self):

        return self.libro.titulo