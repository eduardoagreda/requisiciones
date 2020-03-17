from rest_framework.serializers import ModelSerializer

from apps.solicitudes.models import Solicitudes
from apps.usuarios.serializers import UsersSerializers
from apps.profesores.serializers import ProfesoresSerializers
from apps.materias.serializers import MateriasSerializers
from apps.materiales.serializers import MaterialesSerializers

class SolicitudesSerializers(ModelSerializer):
    usuario = UsersSerializers(read_only=True)
    profesor = ProfesoresSerializers(read_only=True)
    materias = MateriasSerializers(read_only=True)
    materiales = MaterialesSerializers(read_only=True)

    class Meta:
        model = Solicitudes
        fields = ('__all__')