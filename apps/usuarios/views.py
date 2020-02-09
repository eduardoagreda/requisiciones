from django.shortcuts import render, get_object_or_404, redirect

from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.usuarios.models import User
from apps.usuarios.forms import UserForm
from apps.usuarios.serializers import UsersSerializers

# Create your views here.

class UsuariosList(APIView):
    def get(self, request):
        usuarios = User.objects.all().filter(is_staff=False)
        if usuarios:
            serializer = UsersSerializers(usuarios, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        result = {'data': 'Error, no se encuentran datos en la base de datos.'}        
        return Response(result, status=status.HTTP_204_NO_CONTENT)

def add_usuarios(request):
    if request.method == 'POST':
        usuarios_form = UserForm(data=request.POST)
        if usuarios_form.is_valid():
            usuarios = usuarios_form.save(commit=False)
            usuarios.save()
            return redirect('lista_usuarios')
    else:
        usuarios_form = UserForm()
    #return render(request=request, template_name='', {'form':usuarios_form})

def edit_usuarios(request, pk):
    usuarios = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        usuarios_form =  UserForm(data=request.POST, instance=usuarios)
        if usuarios_form.is_valid():
            usuarios = usuarios_form.save(commit=False)
            usuarios.save()
            return redirect('lista_usuarios')
    else:
        usuarios_form = UserForm(instance=usuarios)
    #return render (request=request, template_name='', {'form': usuarios_form})

def delete_usuarios(request, pk):
    usuarios = get_object_or_404(User, id=pk)
    if request.method  == 'POST' and 'delete' in request.POST:
        usuarios.delete()
        return redirect ('lista_usuarios')
    elif request.method == 'POST' and 'cancel' in request.POST:
        return redirect('lista_usuarios')
    #return render(request=request, template_name='')

def lista_usuarios(request):
    usuarios = User.objects.all().filter(is_staff=False)
    #return render(request=request, template_name='', {'usuarios':usuarios})