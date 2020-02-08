from django.db import models

# Create your models here.

class Profesor(models.Model):
    CHOICES_GRADO = (
        ('M.C.', 'Maestro en Ciencias'),
        ('DR.', 'Doctor'),
        ('CHEF.', 'CHEF'),
        ('LIC.', 'Licenciado')
    )
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    grado = models.CharField(max_length=6, blank=True, null=True, choices=CHOICES_GRADO)

    def __str__ (self):
        return self.grado + ' ' + self.nombre + ' ' + self.apellidos