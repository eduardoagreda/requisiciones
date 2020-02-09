from rest_framework.serializers import Serializer

from apps.profesores.models import Profesor

class ProfesoresSerializers(Serializer):
    class Meta:
        model = Profesor
        fields = ('__all__')