# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0014_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='apellido_materno',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='apellido_paterno',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='ciudad',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='direccion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
