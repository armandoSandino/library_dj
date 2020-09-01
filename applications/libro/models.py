from django.db import models
# from local apps
from applications.autor.models import Autor
# Manager
from .managers import LibroManager, CategoriaManager

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
    
    # Le indicara a nuestro modelo que trabaje con este administrador
    objects = CategoriaManager()

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nombre

class Libro(models.Model):
    # related_name, El nombre que se utilizará para la relación del objeto relacionado con este.
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ForeignKey.related_name
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria_libro'
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(
        'Titulo',
        max_length=50,
        blank=False
    )
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='libro', blank=False)
    visitas = models.PositiveIntegerField('Visitas', blank=False)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural="Libros"
    
    # Le indicara a nuestro modelo que trabaje con este administrador
    objects = LibroManager()

    def __str__(self):
        return self.titulo