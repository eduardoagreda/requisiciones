from django.db import models

# Create your models here.

class Materia(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    clave = models.CharField(max_length=10, blank=True, null=True)
    creditos = models.IntegerField(blank=True, null=True)

    def __str__ (self):
        return self.nombre