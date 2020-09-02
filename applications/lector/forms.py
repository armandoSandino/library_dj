from django import forms
#Models
from .models import Prestamo

class PrestamoForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro'
        )
