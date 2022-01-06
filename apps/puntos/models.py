from django.db import models
from djgeojson.fields import PointField


# Create your models here.
class Punto(models.Model):
    nombre = models.CharField(
        max_length=1024,
        verbose_name="Nombre Punto")

    direccion = models.CharField(
        max_length=1024,
        verbose_name="Direccion Punto")

    geo_ubicacion = PointField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.direccion )


class AgendaTelefonica(models.Model):
    TIPO_DE_NUMERO = [
        ('PBX', 'Numero PBX con indicativo'),
        ('Fijo', 'Numero fijo'),
        ('Celular', 'Numero celular'),
        ('Whatsapp', 'Whatsapp')
    ]
    punto = models.ForeignKey(
        Punto,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_DE_NUMERO,
        default='Fijo',
    )
    numero = models.CharField(
        max_length=20,
        verbose_name="Numero Contacto")

    def __str__(self):
        return '{} - {}'.format(self.numero, self.tipo)