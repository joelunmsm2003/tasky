# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0016_auto_20150126_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('telefono', models.ForeignKey(to='ticket.Usuarios')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='nombre',
        ),
    ]
