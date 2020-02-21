from django import forms

from apps.solicitudes.models import Solicitudes

from apps.materiales.models import Materiales

from tempus_dominus.widgets import DatePicker, TimePicker

from datetime import date, time

class SolicitudesForm(forms.ModelForm):
    fecha = forms.DateField(widget=DatePicker(
        options= {
            'useCurrent': True,
            'format': 'DD/MM/YYYY',
            'minDate': str(date.today()),
        },
        attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
        }
    ))
    
    hora_inicio = forms.TimeField(
        widget=TimePicker(
            options={
                'useCurrent': True,
                'enabledHours': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                'format': 'HH:mm',
            },
            attrs={
                'append': 'fa fa-clock',
                'icon_toggle': True,
            },
        ),
    )

    hora_fin = forms.TimeField(
        widget=TimePicker(
            options={
                'useCurrent': True,
                'enabledHours': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
                'format': 'HH:mm',
            },
            attrs={
                'append': 'fa fa-clock',
                'icon_toggle': True,
            },
        ),
    )
    materiales = forms.ModelMultipleChoiceField(queryset=Materiales.objects.all().filter(estatus='Disponible'), label='Materiales')
    class Meta:
        model = Solicitudes
        fields = ['fecha', 'hora_inicio', 'hora_fin', 'profesor', 'materia', 'lugar', 'materiales']