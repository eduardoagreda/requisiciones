from rest_framework.serializers import Serializer

from apps.profesores.models import Profesores

class ProfesoresSerializers(Serializer):
    class Meta:
        model = Profesores
        fields = ('__all__')