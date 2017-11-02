# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0031_ticket_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='name',
            field=models.TextField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
