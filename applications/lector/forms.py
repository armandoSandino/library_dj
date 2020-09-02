from django import forms
#Models
from applications.libro.models import Libro
from .models import Prestamo


class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro'
        )

class MultiplePrestamoForm(forms.ModelForm):

    # ModelMultipleChoiceField, nos permite mostrar un conjunto para un modelo en especifico
    # CheckboxSelectMultiple, tipo de control para cada elemento del conjunto
    # queryset, podemos inicializar el conjunto de datos que necesitemos
    libros = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget= forms.CheckboxSelectMultiple,
    )

    class Meta:
        # modelo a trabajar
        model = Prestamo
        # campos del modelo a trabajar
        fields = (
            'lector',
        )

    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        # inicializamos el conjunto de datos con el qu trabajaremos
        self.fields['libros'].queryset = Libro.objects.all()
