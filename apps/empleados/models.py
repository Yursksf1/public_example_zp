from django.db import models


# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(
        max_length=1024,
        verbose_name="Nombre Empleado")

    apellido = models.CharField(
        max_length=1024,
        verbose_name="Apellido Empleado")

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

class AgendaTelefonica(models.Model):
    TIPO_DE_NUMERO = [
        ('Fijo', 'Numero fijo'),
        ('Celular', 'Numero celular')
    ]
    empleado = models.ForeignKey(
        Empleado,
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