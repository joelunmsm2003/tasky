# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0030_chat_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='empresa',
            field=models.ForeignKey(default=1, to='ticket.Empresa'),
            preserve_default=False,
        ),
    ]
