from django.contrib import admin

# Register your models here.

from apps.solicitudes.models import Solicitudes

admin.site.register(Solicitudes)