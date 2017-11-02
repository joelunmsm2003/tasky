# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0034_auto_20150528_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='version',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
