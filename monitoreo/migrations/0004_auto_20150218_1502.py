# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0003_rango'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='rango',
            name='caracteristica',
            field=models.ForeignKey(to='monitoreo.Caracteristica'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rango',
            name='tipo',
            field=models.ForeignKey(to='monitoreo.Tipo'),
            preserve_default=True,
        ),
    ]
