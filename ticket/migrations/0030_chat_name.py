# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0029_auto_20150504_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
