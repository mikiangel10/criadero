# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0002_auto_20171010_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='anotaciones',
            name='postura',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
