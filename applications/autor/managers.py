# Models
from django.db import models 

class AutorManager(models.Manager):
    ''' Manager para el modelo Autor '''

    def listar_autores(self):
        # El self.all() seria igual a utilizar desde la vista Autor.objects.all()
        return self.all()