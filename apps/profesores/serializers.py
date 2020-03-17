from rest_framework import serializers

from apps.profesores.models import Profesor

class ProfesoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('__all__')