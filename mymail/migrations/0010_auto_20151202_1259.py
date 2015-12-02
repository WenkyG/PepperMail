# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0009_trash_m_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trash',
            name='m_id',
            field=models.IntegerField(default=0),
        ),
    ]
