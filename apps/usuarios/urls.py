from django.urls import path

from apps.usuarios.views import add_usuarios, edit_usuarios, delete_usuarios, lista_usuarios
from apps.usuarios.views import ListUsuarios, dashboard, index

from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('usuario/crear/', add_usuarios, name='add_usuarios'),
    path('usuario/<int:pk>/editar/', edit_usuarios, name='edit_usuarios'),
    path('usuario/<int:pk>/eliminar/', delete_usuarios, name='delete_usuarios' ),
    path('usuarios/listar/', lista_usuarios, name='lista_usuarios'),
    path('api/usuarios/listar/', ListUsuarios.as_view()),
    path('account/login/', LoginView.as_view(), name='login'),
    path('account/logout/', LogoutView.as_view(next_page='index'), name="logout"),
]
