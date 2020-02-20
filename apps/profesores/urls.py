from django.urls import path

from apps.profesores.views import add_profesores, edit_profesores, delete_profesores, lista_profesores, ProfesoresList, DetalleProfesor, DeleteProfesor

urlpatterns = [
    path('profesor/crear/', add_profesores, name='add_profesores'),
    path('profesor/<int:pk>/editar/', edit_profesores, name='edit_profesores'),
    path('profesor/<int:pk>/eliminar/', DeleteProfesor.as_view(), name='delete_profesores'),
    path('profesor/<int:pk>/detalle/', DetalleProfesor.as_view(), name='read_profesores'),
    path('profesores/listar/', lista_profesores, name='lista_profesores'),
    path('api/profesores/listar/', ProfesoresList.as_view()),
]
