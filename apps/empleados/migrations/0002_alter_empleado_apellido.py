# Generated by Django 4.0 on 2021-12-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='apellido',
            field=models.CharField(max_length=1024, verbose_name='Apellido Empleado'),
        ),
    ]
