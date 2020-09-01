
import datetime
# Models
from django.db import models
from django.db.models import Q

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

    # Buscar libro por su titulo y rango de fechas
    def buscar_libro_x_rango_fecha(self, termino, fecha_inicial, fecha_final ):

        # Formatear la fechas al formato correcto
        fe_inicial = datetime.datetime.strptime( fecha_final,"%Y-%m-%d").date()
        fe_final = datetime.datetime.strptime( fecha_final, "%Y-%m-%d").date()

        resultado = self.filter(
            titulo__icontains=termino,
            fecha__range=(fe_inicial, fecha_final)
        )

        return resultado

    # Listar libros por categoria
    def listar_libros_categoria(self, id_categoria ):
        # 'categoria' es una llave foranea en Libro y 'id' es el identificador en la tabla Categoria
        return self.filter(
            categoria__id=id_categoria
        ).order_by('titulo') 

    def agregar_autor_libro(self, id_libro, autor ):
        # Obtenemos el libro
        libro = self.get(id=id_libro)
        # Agregamos datos, pero tambien podrias borrar al cambiar 'add' por 'remove'
        libro.autores.add( autor )

        return libro


class CategoriaManager(models.Manager):
    # categoria_libro, es un campo de 'Categoria(modelo/tabla)' 
    # proporcionado por el modelo 'Libro' mediante el atributo 'related_name'
    # distinct(), nos permitira obtener registros no  repetidos
    def categoria_por_autor(self, autor ):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()

