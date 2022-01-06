# Generated by Django 4.0 on 2021-12-22 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puntos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendatelefonica',
            name='tipo',
            field=models.CharField(choices=[('PBX', 'Numero PBX con indicativo'), ('Fijo', 'Numero fijo'), ('Celular', 'Numero celular'), ('Whatsapp', 'Whatsapp')], default='Fijo', max_length=10),
        ),
    ]
