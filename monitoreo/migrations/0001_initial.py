# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0021_auto_20150209_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('descripcion', models.CharField(max_length=120)),
                ('ubicacion', models.CharField(max_length=120)),
                ('empresa', models.ForeignKey(to='ticket.Empresa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip', models.CharField(max_length=120)),
                ('puerto_origen', models.CharField(max_length=120)),
                ('puerto_final', models.CharField(max_length=120)),
                ('tipo', models.CharField(max_length=120)),
                ('servicio', models.CharField(max_length=120)),
                ('user', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('equipo', models.ForeignKey(to='monitoreo.Equipos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
