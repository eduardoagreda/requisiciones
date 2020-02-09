from django.urls import path

from apps.materiales.views import add_materiales, edit_materiales, lista_materiales, delete_materiales, MaterialesList

urlpatterns = [
    path('materiales/crear/', add_materiales, name='add_materiales'),
    path('materiales/<int:pk>/editar/', edit_materiales, name='edit_materiales'),
    path('materiales/<int:pk>/eliminar/', delete_materiales, name='delete_materiales'),
    path('materiales/listar/', lista_materiales, name='lista_materiales'),
    path('api/materiales/listar/', MaterialesList.as_view()),
]
