# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0002_mailing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='receiver',
            field=models.ForeignKey(related_name='receive', to='mymail.user'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='sender',
            field=models.ForeignKey(related_name='send', to='mymail.user'),
        ),
    ]
