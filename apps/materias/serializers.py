from rest_framework.serializers import Serializer

from apps.materias.models import Materias

class MateriasSerializers(Serializer):
    class Meta:
        model = Materias
        fields = ('__all__')