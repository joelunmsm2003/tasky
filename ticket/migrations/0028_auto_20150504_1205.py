# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0027_chat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='chat',
            new_name='chat_c',
        ),
        migrations.AddField(
            model_name='chat',
            name='chat_s',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
