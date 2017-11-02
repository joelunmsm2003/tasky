# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0032_auto_20150526_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='descripcion',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
