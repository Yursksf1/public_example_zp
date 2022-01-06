from django.shortcuts import render
from apps.puntos.models import Punto
from apps.llamadas.controller import PuntoController, AgendaTelefonicaController, RegistroLlamadaController
from django.http import JsonResponse

# Create your views here.

def index(request):
    puntos = PuntoController.get_all_puntos()

    context = {
        'puntos': puntos,
    }
    return render(
        request,
        'index.html',
        context
    )

def render_template_base(request):
    puntos = PuntoController.get_all_puntos()

    context = {
        'puntos': puntos,
    }
    return render(
        request,
        'template_base.html',
        context
    )


def get_all_puntos(request):
    puntos = PuntoController.get_all_puntos()
    context = {
        'puntos': puntos,
    }
    return JsonResponse(puntos, safe=False)


def contesto(request, id):
    RegistroLlamadaController.cambiar_estado_contestado(id)
    data = {
        'message': 'ok'
    }
    return JsonResponse(data)

def no_contesto(request, id):
    RegistroLlamadaController.cambiar_estado_no_contestado(id)
    data = {
        'message': 'ok'
    }
    return JsonResponse(data)

def edit(request, id):
    RegistroLlamadaController.cambiar_estado_edito(id)
    data = {
        'message': 'ok'
    }
    return JsonResponse(data)


def llamando(request, id):
    RegistroLlamadaController.cambiar_estado_llamando(id)
    data = {
        'message': 'ok'
    }
    return JsonResponse(data)


def historico(request):
    print('aca va el historico')
    context = {}
    return render(
        request,
        'historico.html',
        context
    )

#
# def llamando(request):
#     data = {}
#     if request.method == 'POST':
#         payload = request.POST
#         id = payload.get('id')
#
#         choise = payload.get('choise')
#
#         telefono = AgendaTelefonicaController.get_telefono_by_id(id)
#         if not telefono:
#             data = {'message': 'error, telefono no found'}
#             return JsonResponse(data)
#
#         registro_llamada = RegistroLlamadaController.get_registro_llamada_hoy(telefono.id)
#         if not registro_llamada:
#             print('no hay registro llamada, voy a crear una')
#             registro_llamada = RegistroLlamadaController.crear_registro(telefono)
#             data = {'message': 'listo cree el registro'}
#             return JsonResponse(data)
#
#
#     return JsonResponse(data)

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PuntoSerializer, AgendaTelefonicaSerializer, RegistroLlamadaSerializer


class PuntoView(viewsets.ModelViewSet):
    serializer_class = PuntoSerializer
    queryset = Punto.objects.all()