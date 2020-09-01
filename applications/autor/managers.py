# Models
from django.db import models 
# Q Permitira realizar consultas condicionadas ( or, || )
from django.db.models import Q

class AutorManager(models.Manager):
    ''' Manager para el modelo Autor '''

    def listar_autores(self):
        # El self.all() seria igual a utilizar desde la vista Autor.objects.all()
        return self.all()

    # Busca un autor por su nombre    
    def buscar_autor(self, autor_a_buscar):
        # Recurde que el __icontains busca conincidencias( like ) en un campo
        resultado = self.filter(
            nombre__icontains= autor_a_buscar
        )
        return resultado
    
    def buscar_author_x_nombre_or_apellido(self, autor_a_buscar):
        # Q funciona como un 'or' para las condicionales
        return self.filter(
            Q(nombre__icontains=autor_a_buscar) |  Q(apellidos__icontains=autor_a_buscar)
        )

    # Buscar autor tomando en cuenta su edad
    def buscar_author_determinado(self, termino ):
        # exclude excluye los registros expecificados en su clausula
        return self.filter(
            nombre__icontains = termino
        ).exclude(
            Q(edad__icontains=26) | Q(edad__icontains=33)
        )

    def buscar_autor_x_edad(self, term ):
        # Para la condicional and puedes utilizar __gt  y __lt
        # order_by, ordena en base a determinados campos
        res = self.filter(
            edad__gt=25,
            edad__lt=26
        ).order_by('apellidos','nombre','id')

        return res  


