# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0009_auto_20171029_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Fechas',
            },
        ),
        migrations.AlterModelOptions(
            name='anotacion',
            options={'verbose_name_plural': 'Anotaciones'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': 'Colores'},
        ),
        migrations.AlterModelOptions(
            name='galpon',
            options={'verbose_name_plural': 'Galpones'},
        ),
        migrations.AlterModelOptions(
            name='plantel',
            options={'verbose_name_plural': 'Planteles'},
        ),
        migrations.AddField(
            model_name='anotacion',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2018, 1, 7, 18, 57, 32, 772736, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anotacion',
            name='fecha',
            field=models.ForeignKey(to='sitio.Fecha'),
        ),
    ]
