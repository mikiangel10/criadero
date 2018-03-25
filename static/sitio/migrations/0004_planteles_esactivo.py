# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0003_anotaciones_postura'),
    ]

    operations = [
        migrations.AddField(
            model_name='planteles',
            name='esactivo',
            field=models.IntegerField(default=0),
        ),
    ]
