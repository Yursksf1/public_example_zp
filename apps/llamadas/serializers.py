
from rest_framework import serializers
from apps.llamadas.models import RegistroLlamada
from apps.puntos.models import Punto, AgendaTelefonica


class PuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punto
        fields = ('id', 'nombre', 'direccion', 'geo_ubicacion')


class AgendaTelefonicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaTelefonica
        fields = ('id', 'punto', 'tipo', 'numero')


class RegistroLlamadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroLlamada
        fields = ('id', 'punto', 'numero', 'estado', 'created_date')