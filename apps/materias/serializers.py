from rest_framework.serializers import Serializer

from apps.materias.models import Materia

class MateriasSerializers(Serializer):
    class Meta:
        model = Materia
        fields = ('__all__')