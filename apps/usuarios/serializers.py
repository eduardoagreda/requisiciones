from rest_framework import serializers

from apps.usuarios.models import User

class UsersSerializers(serializers.Serializer):
    class Meta:
        model = User
        fields = ('__all__')