# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0004_auto_20150218_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Red',
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
            name='red',
            field=models.ForeignKey(to='monitoreo.Red'),
            preserve_default=True,
        ),
    ]
