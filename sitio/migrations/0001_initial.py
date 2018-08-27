# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-27 23:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anotacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('muertes', models.IntegerField(default=0)),
                ('postura', models.IntegerField(default=0)),
                ('comentario', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Anotaciones',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Colores',
            },
        ),
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name_plural': 'Fechas',
            },
        ),
        migrations.CreateModel(
            name='Galpon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('produccion', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Galpones',
            },
        ),
        migrations.CreateModel(
            name='Plantel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('es_activo', models.BooleanField(default=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('nacimiento', models.DateField(default=datetime.date.today)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Color')),
                ('galpon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Galpon')),
            ],
            options={
                'verbose_name_plural': 'Planteles',
            },
        ),
        migrations.AddField(
            model_name='anotacion',
            name='fecha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Fecha'),
        ),
        migrations.AddField(
            model_name='anotacion',
            name='plantel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.Plantel'),
        ),
        migrations.AddField(
            model_name='anotacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
