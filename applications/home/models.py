from django.db import models

class Persona(models.Model):
    """ Todo por una persona """
    full_name = models.CharField('Nombres', max_length=50, blank=False)
    pais = models.CharField('Pais', max_length=30, blank=False)
    pasaporte =  models.CharField('Pasaporte', max_length=50, blank=False)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10, blank=False)

    class Meta:

        verbose_name = 'La Persona'
        verbose_name_plural = 'Las Personas'
        # Especificar el nombre con el que se creara el Modelo/Tabla en nuestra base de datos mediante 'db_table'
        # Si no se especifica por defecto tomara el nombre de la aplicacion concatenado con el nombre del modelo
        # Ej. home_persona
        db_table = 'Mi_tabla_persona'
        
        # Evitar que se agregue registros con el mismo valor para un determinado campo mediante 'unique_together'
        unique_together = ['pais', 'apelativo']

        # Evitar que se agregue registros con la edad de 18
        # El 'gte' significa mayor o igual
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_de_18')
        ]

        # Le indicara al ORM de Django que este modelo sera una clase Abstracta de la cual extenderan otros modelos
        # Por lo cual podemos indicarle que no se cree en la base de datos
        # abstract = True

    def __str__(self):
        return self.full_name


class Empleado(Persona):
    
    empleo = models.CharField('Empleo', max_length=50, blank=False)


