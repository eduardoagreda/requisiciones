from django.urls import path

from apps.materias.views import add_materias, delete_materias, edit_materias, lista_materias, ListMateria, DetalleMateria

urlpatterns = [
    path('materia/crear/', add_materias, name='add_materias'),
    path('materia/<int:pk>/editar/', edit_materias, name='edit_materias'),
    path('materia/<int:pk>/eliminar/', delete_materias, name='delete_materias'),
    path('materia/<int:pk>/detalle/', DetalleMateria.as_view(), name='read_materias'),
    path('materias/listar/', lista_materias, name='lista_materias'),
    path('api/materias/listar/', ListMateria.as_view()),
]
