# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0008_auto_20151202_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='trash',
            name='m_id',
            field=models.IntegerField(default=0, max_length=25),
        ),
    ]
