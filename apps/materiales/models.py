from django.db import models

# Create your models here.

class Materiales(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estatus = models.CharField(max_length=30, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    surtido = models.IntegerField(blank=True, null=True)

    def __str__ (self):
        return self.nombre 