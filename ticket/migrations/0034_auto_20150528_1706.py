# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0033_auto_20150528_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='descripcion',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
