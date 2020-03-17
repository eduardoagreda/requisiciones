from rest_framework.serializers import ModelSerializer

from apps.materias.models import Materia

class MateriasSerializers(ModelSerializer):
    class Meta:
        model = Materia
        fields = ('__all__')