from django import forms

from apps.materiales.models import Materiales

class MaterialesForm(forms.ModelForm):
    class Meta:
        model = Materiales
        fields = ['nombre','descripcion','estatus','stock','surtido']