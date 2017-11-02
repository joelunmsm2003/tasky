# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0022_auto_20150216_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(max_length=100, serialize=False, primary_key=True)),
                ('telefono', models.CharField(max_length=1000, blank=True)),
                ('tipo', models.CharField(max_length=1000, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
