# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0018_telefono_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='evento',
            field=models.ForeignKey(to='ticket.Ticket'),
            preserve_default=True,
        ),
    ]
