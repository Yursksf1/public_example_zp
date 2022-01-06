#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Django
from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.puntos.models import Punto, AgendaTelefonica

mapping_id = {
    "1": "Ziru's Calle 56",
    "2": "Ziru's Lagos",
    "3": "Ziru's Riviera",
    "4": "Ziru's Paralela",
    "5": "Ziru's Girón",
    "6": "Ziru's Piedecuesta",
}

lista_populate_puntos = [
  ["1", "Ziru's Calle 56", "Calle 56 No 30-48", ],
  ["2", "Ziru's Lagos", "Glorieta parque caracolí, Round point lagos 1. Local 9, cra 24 13-14", ],
  ["3", "Ziru's Riviera", "Calle 33 31-107", ],
  ["4", "Ziru's Paralela", "Autopista Florida No. 147-51", ],
  ["5", "Ziru's Girón", "Calle 30 No. 27-03 Casco Antiguo", ],
  ["6", "Ziru's Piedecuesta", "Autopista 5ta granada Av. 7 15-05", ],
]

lista_populate_telefono = [
    ["1", "PBX", "6410000-1"],
    ["1", "Fijo", "6960171"],
    ["1", "Celular", "3164726225"],
    ["1", "Whatsapp", "3164726225"],

    ["2", "PBX", "6410000-2", ],
    ["2", "Fijo", "6199925", ],
    ["2", "Celular", "3174006144"],
    ["2", "Whatsapp", "3174006144"],

    ["3", "PBX", "6410000-3", ],
    ["3", "Fijo", "6351768"],
    ["3", "Celular", "3187205106"],
    ["3", "Whatsapp", "3187205106"],

    ["4", "PBX", "6410000-4", ],
    ["4", "Fijo", "6199923"],
    ["4", "Celular", "3176468038"],
    ["4", "Whatsapp", "3176468038"],

    ["5", "PBX", "6410000-5", ],
    ["5", "Fijo", "6133721"],
    ["5", "Celular", "3152491231"],
    ["5", "Whatsapp", "3152491231"],

    ["6", "PBX", "6410000-6", ],
    ["6", "Fijo", "6909569"],
    ["6", "Celular", "3175905867"],
    ["6", "Whatsapp", "3175905867"],
]


class Command(BaseCommand):
    def handle(self, *args, **options):

        for index, row in enumerate(lista_populate_puntos):
            p = Punto()
            p.nombre = row[1]
            p.direccion = row[2]
            p.save()

        for index, row in enumerate(lista_populate_telefono):
            p = Punto.objects.filter(
                nombre=mapping_id.get(row[0])
            ).first()

            at = AgendaTelefonica()
            at.punto = p
            at.tipo = row[1]
            at.numero = row[2]
            at.save()
