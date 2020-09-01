# Models
from django.db import models 

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