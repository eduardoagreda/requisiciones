from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy

from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.profesores.models import Profesor
from apps.profesores.forms import ProfesorForm
from apps.profesores.serializers import ProfesoresSerializers

from django.views.generic import DetailView, DeleteView

# Create your views here.

class ProfesoresList(APIView):
    def get(self, request):
        profesores = Profesor.objects.all()
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
    return render(request, 'profesores/create.html', {'form':profesores_form})

def edit_profesores(request, pk):
    profesores = get_object_or_404(Profesor, id=pk)
    if request.method == 'POST':
        profesores_form =  ProfesorForm(data=request.POST, instance=profesores)
        if profesores_form.is_valid():
            profesores = profesores_form.save(commit=False)
            profesores.save()
            return redirect('lista_profesores')
    else:
        profesores_form = ProfesorForm(instance=profesores)
    return render (request, 'profesores/update.html', {'form': profesores_form})

def delete_profesores(request, pk):
    profesores = get_object_or_404(Profesor, id=pk)
    if request.method  == 'POST':
        profesores.delete()
        return redirect ('lista_profesores')
    return render(request, 'profesores/delete.html')

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores/list.html', {'profesores':profesores})

class DetalleProfesor(DetailView):
    model = Profesor
    template_name = 'profesores/read.html'

class DeleteProfesor(DeleteView):
    model = Profesor
    template_name = 'profesores/delete.html'
    success_url = reverse_lazy('lista_profesores')