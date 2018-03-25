# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0004_planteles_esactivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planteles',
            name='esactivo',
        ),
        migrations.AddField(
            model_name='planteles',
            name='es_activo',
            field=models.BooleanField(default=0),
        ),
    ]
