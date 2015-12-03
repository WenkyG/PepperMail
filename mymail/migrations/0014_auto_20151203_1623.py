# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0013_mailing_vistited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailing',
            name='vistited',
        ),
        migrations.AddField(
            model_name='mailing',
            name='vistied',
            field=models.BooleanField(default=False),
        ),
    ]
