# Generated by Django 4.1 on 2022-11-10 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_artistas_data_alter_artistas_nombre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artistas',
            options={'ordering': ['fecha_reg']},
        ),
        migrations.AlterField(
            model_name='artistas',
            name='data',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
