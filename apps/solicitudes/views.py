from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from django.urls import reverse_lazy

from django.core.mail import send_mail, EmailMultiAlternatives

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib import messages 

from django.views.generic import DetailView, DeleteView

from apps.materiales.models import Materiales

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
            return Response(data={'solicitudes':serializer.data}, status=status.HTTP_200_OK)
        result = {'data': 'Error, no se encuentran datos en la base de datos.'}        
        return Response(result, status=status.HTTP_204_NO_CONTENT)

@login_required
def add_solicitudes(request):
    materiales = Materiales.objects.all()
    if request.method == 'POST':
        solicitudes_form = SolicitudesForm(request.POST)
        if solicitudes_form.is_valid():
            solicitudes = solicitudes_form.save(commit=False)
            if solicitudes.hora_fin < solicitudes.hora_inicio:
                messages.error(request, 'El horario no está bien asignado')
                return render(request, 'solicitudes/create.html', {'form':solicitudes_form, 'materiales': materiales})
            else:
                solicitudes.usuario = request.user
                print(solicitudes)
                solicitudes.save()
                solicitudes_form.save_m2m()
                content = "<p>El usuario  " + '<strong>' +solicitudes.usuario.first_name +" "+ solicitudes.usuario.last_name + "</strong>  ha solicitado la requisición de materiales número: <strong>" + str(solicitudes.id) + "</strong>, el día: <strong>" + str(solicitudes.fecha) + "</strong> para la materia de <strong>" + str(solicitudes.materia) + "</strong> que impartirá el docente: <strong>" + solicitudes.profesor.nombre + ' ' + solicitudes.profesor.apellidos + "</strong>; la cual se llevará acabo en la cocina: <strong>" + solicitudes.lugar + "</strong> con hora de inicio a las: <strong>" + str(solicitudes.hora_inicio) + "</strong>  y finalizara a las: <strong>" + str(solicitudes.hora_fin) + "</strong>.<br>El estado de la requisición es: <strong>" + solicitudes.estatus + '</strong>.</p>'
                mailto = EmailMultiAlternatives(subject='Requisición número: ' + str(solicitudes.id), 
                    body='', from_email=None,
                    to=[solicitudes.usuario.email, 'beeve3108@gmail.com']
                )
                mailto.attach_alternative(content=content, mimetype='text/html')
                mailto.send()
            return redirect('lista_solicitudes')
    else:
        solicitudes_form = SolicitudesForm()
        return render(request, 'solicitudes/create.html', {'form':solicitudes_form, 'materiales': materiales})
    return render(request, 'solicitudes/create.html', {'form':solicitudes_form, 'materiales': materiales})

@login_required
def edit_solicitudes(request, pk):
    solicitudes = get_object_or_404(Solicitudes, id=pk)
    if request.method == 'POST':
        solicitudes_form =  SolicitudesForm(request.POST, instance=solicitudes)
        if solicitudes_form.is_valid():
            solicitudes = solicitudes_form.save(commit=False)
            if solicitudes.hora_fin < solicitudes.hora_inicio:
                messages.error(request, 'El horario no está bien asignado')
                return render(request, 'solicitudes/create.html', {'form':solicitudes_form})
            if solicitudes.estatus == 'Aceptada':
                content = "<p>El usuario  " + '<strong>' +solicitudes.usuario.first_name +" "+ solicitudes.usuario.last_name + "</strong>  ha solicitado la requisición de materiales número: <strong>" + str(solicitudes.id) + "</strong>, el día: <strong>" + str(solicitudes.fecha) + "</strong> para la materia de <strong>" + str(solicitudes.materia) + "</strong> que impartirá el docente: <strong>" + solicitudes.profesor.nombre + ' ' + solicitudes.profesor.apellidos + "</strong>; la cual se llevará acabo en la cocina: <strong>" + solicitudes.lugar + "</strong> con hora de inicio a las: <strong>" + str(solicitudes.hora_inicio) + "</strong>  y finalizara a las: <strong>" + str(solicitudes.hora_fin) + "</strong>.<br>El estado de la requisición es: <strong>" + solicitudes.estatus + '</strong>.</p>'
                mailto = EmailMultiAlternatives(subject='Requisición número: ' + str(solicitudes.id), 
                    body='', from_email=None,
                    to=[solicitudes.usuario.email, 'beeve3108@gmail.com']
                )
                mailto.attach_alternative(content=content, mimetype='text/html')
                mailto.send()
            elif solicitudes.estatus == 'Rechazada':
                solicitudes.activo = True
                content = "<p>El usuario  " + '<strong>' +solicitudes.usuario.first_name +" "+ solicitudes.usuario.last_name + "</strong>  ha solicitado la requisición de materiales número: <strong>" + str(solicitudes.id) + "</strong>, el día: <strong>" + str(solicitudes.fecha) + "</strong> para la materia de <strong>" + str(solicitudes.materia) + "</strong> que impartirá el docente: <strong>" + solicitudes.profesor.nombre + ' ' + solicitudes.profesor.apellidos + "</strong>; la cual se llevará acabo en la cocina: <strong>" + solicitudes.lugar + "</strong> con hora de inicio a las: <strong>" + str(solicitudes.hora_inicio) + "</strong>  y finalizara a las: <strong>" + str(solicitudes.hora_fin) + "</strong>.<br>El estado de la requisición es: <strong>" + solicitudes.estatus + '</strong>.</p>'
                mailto = EmailMultiAlternatives(subject='Requisición número: ' + str(solicitudes.id), 
                    body='', from_email=None,
                    to=[solicitudes.usuario.email, 'beeve3108@gmail.com']
                )
                mailto.attach_alternative(content=content, mimetype='text/html')
                mailto.send()
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

class DetalleSolicitudes(DetailView):
    model = Solicitudes
    template_name = 'solicitudes/read.html'

class DeleteSolicitudes(DeleteView):
    model = Solicitudes
    template_name = 'solicitudes/delete.html'
    success_url = reverse_lazy('lista_solicitudes')