from django.db import models
# from local apps
from applications.autor.models import Autor
# Manager
from .managers import LibroManager

class Categoria(models.Model):
    """Model definition for Categoria."""

    nombre = models.CharField(
        'Nombre',
        max_length=30,
        blank=False
    )

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria del libro'
        verbose_name_plural = 'Categoria de libros'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(
        'Titulo',
        max_length=50,
        blank=False
    )
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada', blank=False)
    visitas = models.PositiveIntegerField('Visitas', blank=False)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural="Libros"
    
    # Le indicara a nuestro modelo que trabaje con este administrador
    objects = LibroManager()

    def __str__(self):
        return self.titulo