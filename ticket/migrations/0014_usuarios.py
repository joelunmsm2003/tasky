# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('ticket', '0013_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, to=settings.AUTH_USER_MODEL)),
                ('usuario_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.TextField()),
                ('apellido_paterno', models.TextField()),
                ('apellido_materno', models.TextField(null=True)),
                ('direccion', models.TextField(null=True)),
                ('ciudad', models.TextField(null=True)),
                ('empresa', models.ForeignKey(to='ticket.Empresa')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
    ]
