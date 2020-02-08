from rest_framework.serializers import Serializer

from apps.usuarios.models import User

class UsersSerializers(Serializer):
    class Meta:
        model = User
        fields = ('__all__')