from _datetime import datetime
from django.db import models
from django.db.models import Q

from apps.puntos.models import Punto, AgendaTelefonica
from apps.llamadas.models import RegistroLlamada

class PuntoController():

    @staticmethod
    def get_all_puntos():
        data = []
        now = datetime.today()

        puntos = Punto.objects.all()
        for punto in puntos:
            llamadas = punto.registrollamada_set.filter(
                created_date__year=now.year,
                created_date__month=now.month,
                created_date__day=now.day,
            )
            obj_serialize = {
                'id': punto.id,
                'nombre': punto.nombre,
                'todos_llamados': False,
            }
            agenda_list = []
            for agenda in punto.agendatelefonica_set.all():
                agenda_list.append(
                    {
                        'id': agenda.id,
                        'tipo': agenda.tipo,
                        'numero': agenda.numero.split('-')[0] if agenda.tipo == 'PBX' else agenda.numero,
                        'extencion': agenda.numero.split('-')[1] if agenda.tipo == 'PBX' else '',
                        'estado_llamada': llamadas.filter(numero=agenda.id).first() and llamadas.filter(
                            numero=agenda.id).first().estado
                    }
                )
            obj_serialize['agenda'] = agenda_list

            llamadas_hoy = []
            for llamada in llamadas.all():
                llamadas_hoy.append(
                    {
                        'id': llamada.id,
                        'tipo': llamada.estado,
                        'numero': str(llamada.numero),
                        'fecha': llamada.created_date
                    }
                )
            obj_serialize['llamadas_hoy'] = llamadas_hoy

            data.append(
                obj_serialize
            )

        return data

    @staticmethod
    def get_punnto_by_id(pk):
        punto = Punto.objects.filter(pk=pk).first()

        return punto

class AgendaTelefonicaController():

    @staticmethod
    def get_telefono_by_id(pk):
        telefono = AgendaTelefonica.objects.filter(pk=pk).first()

        return telefono

class RegistroLlamadaController():

    @staticmethod
    def get_registro_llamada_hoy(telefono_id):
        now = datetime.today()

        llamada = RegistroLlamada.objects.filter(
                numero__id=telefono_id,
                created_date__year=now.year,
                created_date__month=now.month,
                created_date__day=now.day,
        ).first()

        return llamada

    @staticmethod
    def crear_registro(telefono):
        now = datetime.today()

        llamada = RegistroLlamada()
        llamada.punto = telefono.punto
        llamada.numero = telefono
        llamada.estado = 'Llamando'
        llamada.save()

        return llamada

    @staticmethod
    def cambiar_estado_contestado(id):
        now = datetime.today()

        llamada = RegistroLlamada.objects.filter(
            created_date__year=now.year,
            created_date__month=now.month,
            created_date__day=now.day,
            numero=id,
            estado='Llamando'
        ).first()
        llamada.estado = 'Contestado'
        llamada.save()

    @staticmethod
    def cambiar_estado_no_contestado(id):
        now = datetime.today()

        llamada = RegistroLlamada.objects.filter(
            created_date__year=now.year,
            created_date__month=now.month,
            created_date__day=now.day,
            numero=id,
            estado='Llamando'
        ).first()
        llamada.estado = 'Sin Contestar'
        llamada.save()

    @staticmethod
    def cambiar_estado_edito(id):
        now = datetime.today()
        llamada = RegistroLlamada.objects.filter(
            Q(estado='Sin Contestar') | Q(estado='Contestado')
        ).filter(
            created_date__year=now.year,
            created_date__month=now.month,
            created_date__day=now.day,
            numero=id,
        ).first()
        if llamada:
            llamada.estado = 'Llamando'
            llamada.save()


    @staticmethod
    def cambiar_estado_llamando(id):
        now = datetime.today()

        llamada = RegistroLlamada.objects.filter(
            created_date__year=now.year,
            created_date__month=now.month,
            created_date__day=now.day,
            numero=id,
        ).first()
        if llamada:
            llamada.estado = 'Llamando'
            llamada.save()
        else:
            telefono = AgendaTelefonicaController.get_telefono_by_id(id)
            RegistroLlamadaController.crear_registro(telefono)




