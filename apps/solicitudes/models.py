from django.db import models

from apps.usuarios.models import User
from apps.profesores.models import Profesor
from apps.materias.models import Materia
from apps.materiales.models import Materiales

# Create your models here.

class Solicitudes(models.Model):
    CHOICES_ESTATUS = (
        ('Aceptada', 'Aceptada'),
        ('Rechazada', 'Rechazada'),
        ('Reservada', 'Reservada')
    )

    CHOICES_LUGAR = (
        ('Cocina Caliente', 'Cocina Caliente'),
        ('Cocina Fría', 'Cocina Fría'),
        ('Cocina Multiusos', 'Cocina Multiusos'),
        ('Cocina de Humo', 'Cocina de Humo'),
        ('Panadería', 'Panadería'),
    )

    usuario = models.ForeignKey(User, related_name='Usuario', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    hora_inico = models.TimeField(auto_now=False, auto_now_add=False)
    hora_fin = models.TimeField(auto_now=False, auto_now_add=False)
    estatus = models.CharField(max_length=30, blank=True, null=True, choices=CHOICES_ESTATUS)
    profesor = models.ForeignKey(Profesor, related_name='Profesor', on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, related_name='Materia', on_delete=models.CASCADE)
    meteriales = models.ManyToManyField(Materiales, related_name='materiales', verbose_name='materiales')
    lugar = models.CharField(max_length=30, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__ (self):
        return self.profesor + ' - ' + self.materia