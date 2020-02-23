from django.urls import path

from apps.solicitudes.views import add_solicitudes, delete_solicitudes, edit_solicitudes, lista_solicitudes, SolicitudesList, DetalleSolicitudes, DeleteSolicitudes

urlpatterns = [
    path('solicitudes/crear/', add_solicitudes, name='add_solicitudes'),
    path('solicitudes/<int:pk>/editar/', edit_solicitudes, name='edit_solicitudes'),
    path('solicitudes/<int:pk>/eliminar/', DeleteSolicitudes, name='delete_solicitudes'),
    path('solicitudes/<int:pk>/detalle/', DetalleSolicitudes, name='read_solicitudes'),
    path('solicitudes/listar/', lista_solicitudes, name='lista_solicitudes'),
    path('api/solicitudes/listar/', SolicitudesList),
]
