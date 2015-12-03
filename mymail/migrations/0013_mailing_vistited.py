# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0012_auto_20151203_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing',
            name='vistited',
            field=models.BooleanField(default=True),
        ),
    ]
