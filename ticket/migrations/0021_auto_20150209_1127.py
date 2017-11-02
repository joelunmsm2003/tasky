# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0020_document_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='descripcion',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
