# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0004_trash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trash',
            name='receive',
        ),
        migrations.RemoveField(
            model_name='trash',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='trash',
            name='subject',
        ),
    ]
