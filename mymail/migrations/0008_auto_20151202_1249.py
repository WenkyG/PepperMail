# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0007_auto_20151202_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='trash',
            name='receiver',
            field=models.CharField(default=b'mail', max_length=20),
        ),
        migrations.AddField(
            model_name='trash',
            name='sender',
            field=models.CharField(default=b'mail', max_length=20),
        ),
        migrations.AddField(
            model_name='trash',
            name='subject',
            field=models.CharField(default=b'mail', max_length=100),
        ),
        migrations.AlterField(
            model_name='trash',
            name='messege',
            field=models.CharField(default=b'mail', max_length=1000),
        ),
    ]
