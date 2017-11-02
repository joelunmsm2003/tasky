# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0017_auto_20150126_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefono',
            name='tipo',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
