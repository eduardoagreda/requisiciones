from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(AbstractUser):
    semestre = models.CharField(max_length=2, blank=True, null=True)
    grupo = models.CharField(max_length=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #def save(self, request= False, *args, **kwargs):
    #    if not self.pk:
    #       self.password = make_password(self.password)
    #    super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name