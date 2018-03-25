# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anotaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('muertes', models.IntegerField()),
                ('comentario', models.CharField(max_length=200)),
                ('plantel', models.ForeignKey(to='sitio.Planteles')),
            ],
        ),
        migrations.CreateModel(
            name='Privilegios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('ultima', models.DateTimeField(default=datetime.datetime.now)),
                ('priv', models.ForeignKey(to='sitio.Privilegios')),
            ],
        ),
        migrations.AddField(
            model_name='anotaciones',
            name='usuario',
            field=models.ForeignKey(to='sitio.Usuarios'),
        ),
    ]
