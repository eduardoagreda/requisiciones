from rest_framework.serializers import ModelSerializer

from apps.materiales.models import Materiales

class MaterialesSerializers(ModelSerializer):
    class Meta:
        model = Materiales
        fields = ('__all__')