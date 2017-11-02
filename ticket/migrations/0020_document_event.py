# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0019_auto_20150128_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document_Event',
            fields=[
                ('id', models.AutoField(max_length=100, serialize=False, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'files')),
                ('asunto', models.CharField(max_length=100, blank=True)),
                ('fecha_inicio', models.DateTimeField(null=True, blank=True)),
                ('evento', models.ForeignKey(to='ticket.Evento')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
