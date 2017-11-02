# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0025_auto_20150218_1445'),
        ('monitoreo', '0002_equipos_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('red', models.CharField(max_length=120)),
                ('tipo', models.CharField(max_length=120)),
                ('caracteristica', models.CharField(max_length=120)),
                ('ip', models.CharField(max_length=120)),
                ('empresa', models.ForeignKey(to='ticket.Empresa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
