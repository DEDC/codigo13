# Generated by Django 4.1 on 2022-11-29 23:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_artistas_options_alter_artistas_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('folio', models.CharField(editable=False, max_length=25, null=True, unique=True)),
                ('fecha_reg', models.DateTimeField(auto_now_add=True)),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True, editable=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('descripcion', models.TextField()),
                ('lugar', models.CharField(max_length=300, verbose_name='Lugar del evento')),
                ('nombre_cto', models.CharField(max_length=300, verbose_name='Nombre del contacto')),
                ('telefono_cto', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Ingrese un número de teléfono correcto')], verbose_name='Teléfono del contacto')),
                ('correo_cto', models.EmailField(max_length=254, verbose_name='Correo electrónico del contacto')),
                ('artista', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='main.artistas')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
