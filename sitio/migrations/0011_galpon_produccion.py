# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-09 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0010_auto_20180107_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='galpon',
            name='produccion',
            field=models.BooleanField(default=True),
        ),
    ]