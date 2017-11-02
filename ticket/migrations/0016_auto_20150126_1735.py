# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0015_auto_20150126_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='apellido_materno',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='apellido_paterno',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='ciudad',
            field=models.CharField(default=datetime.datetime(2015, 1, 26, 17, 35, 35, 930311), max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='direccion',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
