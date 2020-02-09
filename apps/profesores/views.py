from django.shortcuts import render, get_object_or_404, redirect

from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.profesores.models import Profesor
from apps.profesores.forms import ProfesorForm
from apps.profesores.serializers import ProfesoresSerializers

# Create your views here.

class ProfesoresList(APIView):
    def get(self, request):
        profesores = Materia.objects.all()
        if profesores:
            serializer  = ProfesoresSerializers(profesores, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        result = {'data': 'Error, no se encuentran datos en la base de datos.'}        
        return Response(result, status=status.HTTP_204_NO_CONTENT)

def add_profesores(request):
    if request.method == 'POST':
        profesores_form = ProfesorForm(data=request.POST)
        if profesores_form.is_valid():
            profesores = profesores_form.save(commit=False)
            profesores.save()
            return redirect('lista_profesores')
    else:
        profesores_form = ProfesorForm()
    #return render(request=request, template_name='', {'form':profesores_form})

def edit_profesores(request, pk):
    profesores = get_object_or_404(Materia, id=pk)
    if request.method == 'POST':
        profesores_form =  ProfesorForm(data=request.POST, instance=profesores)
        if profesores_form.is_valid():
            profesores = profesores_form.save(commit=False)
            profesores.save()
            return redirect('lista_profesores')
    else:
        profesores_form = ProfesorForm(instance=profesores)
    #return render (request=request, template_name='', {'form': profesores_form})

def delete_profesores(request, pk):
    profesores = get_object_or_404(Materia, id=pk)
    if request.method  == 'POST' and 'delete' in request.POST:
        profesores.delete()
        return redirect ('lista_profesores')
    elif request.method == 'POST' and 'cancel' in request.POST:
        return redirect('lista_profesores')
    #return render(request=request, template_name='')

def lista_profesores(request):
    profesores = Materia.objects.all()
    #return render(request=request, template_name='', {'profesores':profesores})