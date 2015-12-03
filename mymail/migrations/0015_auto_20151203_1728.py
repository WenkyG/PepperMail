# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0014_auto_20151203_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailing',
            old_name='vistied',
            new_name='visited',
        ),
    ]
