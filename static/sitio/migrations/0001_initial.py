# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Galpones',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Planteles',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField(default=0)),
                ('nacimiento', models.DateField(default=datetime.date.today)),
                ('color', models.ForeignKey(to='sitio.Color')),
                ('galpon', models.ForeignKey(to='sitio.Galpones')),
            ],
        ),
    ]
