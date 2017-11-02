# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0028_auto_20150504_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='chat_c',
            new_name='chat',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='chat_s',
        ),
    ]
