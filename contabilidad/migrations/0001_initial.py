# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-15 13:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
                ('tel', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='', max_length=30)),
                ('cant', models.IntegerField(default=1)),
                ('obs', models.CharField(default='', max_length=50)),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Concepto')),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('monto', models.IntegerField(default=0)),
                ('obs', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('monto', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Sectores',
            },
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='ingreso',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Zona'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Proveedor'),
        ),
        migrations.AddField(
            model_name='concepto',
            name='gasto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Gasto'),
        ),
        migrations.AddField(
            model_name='concepto',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Proveedor'),
        ),
        migrations.AddField(
            model_name='concepto',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Sector'),
        ),
    ]
