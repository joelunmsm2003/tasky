# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0025_auto_20150218_1445'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EstadoObs',
        ),
        migrations.RemoveField(
            model_name='obs',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='obs',
            name='user',
        ),
        migrations.DeleteModel(
            name='Obs',
        ),
        migrations.AddField(
            model_name='ticket',
            name='cancha',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
