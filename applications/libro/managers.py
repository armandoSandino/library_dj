# Models
from django.db import models


class LibroManager(models.Manager):

    def listar_libros(self):
        # El self.all() seria igual a utilizar desde la vista Libro.objects.all()
        return self.all()

    # Busca un libro  
    def buscar_libro(self, termino):
        # Recurde que el __icontains busca conincidencias( like ) en un campo
        # __range, busca registros que este en un rango de fecha, el 1er argumento es la fecha incial el 2do la final
        resultado = self.filter(
            titulo__icontains= termino,
            fecha__range=('2020-01-01', '2020-08-01')
        )
        return resultado