# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0005_auto_20171013_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planteles',
            name='es_activo',
            field=models.BooleanField(default=True),
        ),
    ]
