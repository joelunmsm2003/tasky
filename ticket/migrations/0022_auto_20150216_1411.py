# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0021_auto_20150209_1127'),
    ]

    operations = [
   
        migrations.DeleteModel(
            name='Telefono',
        ),
    ]
