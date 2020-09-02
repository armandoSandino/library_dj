# Models
from django.db import models
from django.db.models import Avg, Sum

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
