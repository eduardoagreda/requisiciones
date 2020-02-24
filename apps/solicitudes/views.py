from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from django.urls import reverse_lazy

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib import messages 

from django.views.generic import DetailView, DeleteView

from apps.solicitudes.models import Solicitudes
from apps.solicitudes.forms import SolicitudesForm
from apps.solicitudes.serializers import SolicitudesSerializers

# Create your views here.

@login_required
class SolicitudesList(APIView):
    def get(self, request):
        solicitudes = Solicitudes.objects.all()
        if solicitudes:
            serializer = SolicitudesSerializers(solicitudes, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        result = {'data': 'Error, no se encuentran datos en la base de datos.'}        
        return Response(result, status=status.HTTP_204_NO_CONTENT)

@login_required
def add_solicitudes(request):
    if request.method == 'POST':
        solicitudes_form = SolicitudesForm(request.POST)
        if solicitudes_form.is_valid():
            solicitudes = solicitudes_form.save(commit=False)
            if solicitudes.hora_fin < solicitudes.hora_inicio:
                messages.error(request, 'El horario no está bien asignado')
                return render(request, 'solicitudes/create.html', {'form':solicitudes_form})
            else:
                solicitudes.usuario = request.user
                solicitudes.save()
                solicitudes_form.save_m2m()
            return redirect('lista_solicitudes')
    else:
        solicitudes_form = SolicitudesForm()
    return render(request, 'solicitudes/create.html', {'form':solicitudes_form})

@login_required
def edit_solicitudes(request, pk):
    solicitudes = get_object_or_404(Solicitudes, id=pk)
    if request.method == 'POST':
        solicitudes_form =  SolicitudesForm(request.POST, instance=solicitudes)
        if solicitudes_form.is_valid():
            solicitudes = solicitudes_form.save(commit=False)
            solicitudes.save()
            solicitudes_form.save_m2m()
            return redirect('lista_solicitudes')
    else:
        solicitudes_form = SolicitudesForm(instance=solicitudes)
    return render (request, 'solicitudes/update.html', {'form': solicitudes_form})

@login_required
def delete_solicitudes(request, pk):
    solicitudes = get_object_or_404(Solicitudes, id=pk)
    if request.method  == 'POST' and 'delete' in request.POST:
        solicitudes.delete()
        return redirect ('lista_solicitudes')
    elif request.method == 'POST' and 'cancel' in request.POST:
        return redirect('lista_solicitudes')
    return render(request, 'solicitudes/delete.html')

@login_required
def lista_solicitudes(request):
    if request.user.is_staff:
        solicitudes = Solicitudes.objects.all()
    else:
        solicitudes = Solicitudes.objects.all().filter(usuario=request.user)
    return render(request, 'solicitudes/list.html', {'solicitudes':solicitudes})

@login_required
class DetalleSolicitudes(DetailView):
    model = Solicitudes
    template_name = 'solicitudes/read.html'

@login_required
class DeleteSolicitudes(DeleteView):
    model = Solicitudes
    template_name = 'solicitudes/delete.html'
    success_url = reverse_lazy('lista_solicitudes')