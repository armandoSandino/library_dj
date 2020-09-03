from django.db import models
from django.db.models.signals import post_save
# apps de terceros
from PIL import Image
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
    # Gestionar las existencias
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "El Libro"
        verbose_name_plural="Los Libros"
        ordering = ['titulo', 'fecha']
    
    # Le indicara a nuestro modelo que trabaje con este administrador
    objects = LibroManager()

    def __str__(self):
        return self.titulo

# sender, donde se enviara/ejecutara la funcion
# instance, instancia en la que se esta trabajando
def optimize_image(sender, instance, **kwargs ):
    print('instance....', instance)
    # Si se cargo un imagen la optimizara
    if instance.portada:
        #Obtenemos la imagen
        portada = Image.open( instance.portada.path )
        # la guardamos optmizada
        portada.save(instance.portada.path, quality=20, optimize=True)

# Se invocara antes que se guarde un registro, en este punto optmizaremos la imagen a almacenar
post_save.connect(optimize_image, sender=Libro)