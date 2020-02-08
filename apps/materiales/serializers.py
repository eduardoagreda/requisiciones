from rest_framework.serializers import Serializer

from apps.materiales.models import Materiales

class MaterialesSerializers(Serializer):
    class Meta:
        model = Materiales
        fields = ('__all__')