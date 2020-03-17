from django.shortcuts import render, get_object_or_404, redirect

from django.http import JsonResponse, Http404

from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.materias.forms import MateriaForm
from apps.materias.serializers import MateriasSerializers
from apps.materias.models import Materia

from django.views.generic import DetailView, DeleteView

# Create your views here.
class ListMateria(APIView):
    def get(self, request, format=None):
        materias = Materia.objects.all()
        if materias:
            serializer  = MateriasSerializers(materias, many=True)
            return Response(data={'materias':serializer.data}, status=status.HTTP_200_OK,)
        result = {'data': 'Error, no se encuentran datos en la base de datos.'}        
        return Response(result, status=status.HTTP_204_NO_CONTENT)

@login_required
def add_materias(request):
    if request.method == 'POST':
        materias_form = MateriaForm(data=request.POST)
        if materias_form.is_valid():
            materias = materias_form.save(commit=False)
            materias.save()
            return redirect('lista_materias')
    else:
        materias_form = MateriaForm()
    return render(request, 'materias/create.html', {'form':materias_form})

@login_required
def edit_materias(request, pk):
    materias = get_object_or_404(Materia, id=pk)
    if request.method == 'POST':
        materias_form =  MateriaForm(data=request.POST, instance=materias)
        if materias_form.is_valid():
            materias = materias_form.save(commit=False)
            materias.save()
            return redirect('lista_materias')
    else:
        materias_form = MateriaForm(instance=materias)
    return render (request, 'materias/update.html', {'form': materias_form})

@login_required
def delete_materias(request, pk):
    materias = get_object_or_404(Materia, id=pk)
    if request.method  == 'POST' and 'delete' in request.POST:
        materias.delete()
        return redirect ('lista_materias')
    elif request.method == 'POST' and 'cancel' in request.POST:
        return redirect('lista_materias')
    return render(request, 'materias/delete.html')

@login_required
def lista_materias(request):
    materias = Materia.objects.all()
    return render(request, 'materias/list.html', {'materias':materias})

class DetalleMateria(DetailView):
    model = Materia
    template_name = 'materias/read.html'

class DeleteMateria(DeleteView):
    model = Materia
    template_name = 'materias/delete.html'
    success_url = reverse_lazy('lista_materias')