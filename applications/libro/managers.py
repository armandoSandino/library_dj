# Models
from django.db import models


class LibroManager(models.Manager):

    def listar_libros(self):
        # El self.all() seria igual a utilizar desde la vista Libro.objects.all()
        return self.all()

    # Busca un libro  
    def buscar_libro(self, termino):
        # Recurde que el __icontains busca conincidencias( like ) en un campo
        resultado = self.filter(
            titulo__icontains= termino
        )
        return resultado