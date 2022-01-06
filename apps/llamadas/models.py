from django.db import models
from django.utils.timezone import now

from apps.puntos.models import Punto, AgendaTelefonica


# Create your models here.
class RegistroLlamada(models.Model):
    TIPO_DE_ESTADO = [
        ('Sin Contestar', 'Sin Contestar'),
        ('Contestado', 'Contestado'),
        ('Llamando', 'Llamando')
    ]

    punto = models.ForeignKey(
        Punto,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    numero = models.ForeignKey(
        AgendaTelefonica,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    estado = models.CharField(
        max_length=20,
        choices=TIPO_DE_ESTADO,
        default='Contestado',
    )

    created_date = models.DateTimeField(default=now, editable=False)

    persona_contesta = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.punto, self.numero, self.numero)