# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0011_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='id',
            field=models.AutoField(max_length=100, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
