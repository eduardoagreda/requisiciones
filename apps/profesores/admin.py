from django.contrib import admin

# Register your models here.

from apps.profesores.models import Profesor

admin.site.register(Profesor)