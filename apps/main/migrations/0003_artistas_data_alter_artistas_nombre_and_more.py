# Generated by Django 4.1 on 2022-11-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_artistas_precio_hora_alter_artistas_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistas',
            name='data',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='artistas',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre del artista'),
        ),
        migrations.AlterField(
            model_name='artistas',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
