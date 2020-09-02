# Models
from django.db import models
from django.db.models import Avg, Sum, Count
from django.db.models.functions import Lower

class PrestamoManager(models.Manager):

    def libros_promedio_lectores_edades(self):
        # Avg, realizara el promedio de la edades de los lectores que prestaron el libro en cuestion
        # Sum,  suma las edades de lectores que prestaron un libro
        resultado = self.filter(
            libro__id=4
        ).aggregate(
            promedio_edad=Avg('lector__edad'),
            suma_edad=Sum('lector__edad')
        )

        return resultado
    
    # Cantidad de veces que se presto un libro
    def numeros_libros_prestados(self):
        # values, no agrupa los registros, en este caso agrupara los resultados de la clausula 'annotate'
        return self.values(
            'libro'
        ).annotate(
            numero_de_veces_prestado=Count('libro'),
            titulo_del_libro=Lower('libro__titulo')
        )
