from django.shortcuts import render, get_object_or_404, redirect

from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.materiales.models import Materiales
from apps.materiales.forms import MaterialesForm
from apps.materiales.serializers import MaterialesSerializers

# Create your views here.

class MaterialesList(APIView):
    def get(self, request):
        materiales = Materiales.objects.all()
        if materiales:
            serializer  = MaterialesSerializers(materiales, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        result = {'data': 'Error, no se encuentran datos en la base de datos.'}        
        return Response(result, status=status.HTTP_204_NO_CONTENT)

def add_materiales(request):
    if request.method == 'POST':
        materiales_form = MaterialesForm(data=request.POST)
        if materiales_form.is_valid():
            materiales = materiales_form.save(commit=False)
            if materiales.stock > 1:
                materiales.estatus = 'Disponible'
            else:
                materiales.estatus = 'Agotado'
            materiales.save()
            return redirect('lista_materiales')
    else:
        materiales_form = MaterialesForm()
    return render(request=request, template_name='materiales/create.html', context={'form': materiales_form})

def edit_materiales(request, pk):
    materiales = get_object_or_404(Materiales, id=pk)
    if request.method == 'POST':
        materiales_form =  MaterialesForm(data=request.POST, instance=materiales)
        if materiales_form.is_valid():
            materiales = materiales_form.save(commit=False)
            if materiales.stock > 1:
                materiales.estatus = 'Disponible'
            else:
                materiales.estatus = 'Agotado'
            materiales.save()
            return redirect('lista_materiales')
    else:
        materiales_form = MaterialesForm(instance=materiales)
    return render (request=request, template_name='materiales/update.html', context={'form': materiales_form})

def delete_materiales(request, pk):
    materiales = get_object_or_404(Materiales, id=pk)
    if request.method  == 'POST' and 'delete' in request.POST:
        materiales.delete()
        return redirect ('lista_materiales')
    elif request.method == 'POST' and 'cancel' in request.POST:
        return redirect('lista_materiales')
    return render(request=request, template_name='materiales/delete.html')

def lista_materiales(request):
    materiales = Materiales.objects.all()
    return render(request=request, template_name='materiales/list.html', context={'materiales':materiales})