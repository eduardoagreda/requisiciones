from django import forms

from apps.materias.models import Materia

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'clave', 'creditos']