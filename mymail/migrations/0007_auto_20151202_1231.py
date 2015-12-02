# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0006_auto_20151202_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trash',
            name='messege',
            field=models.ForeignKey(related_name='msg', on_delete=django.db.models.deletion.DO_NOTHING, to='mymail.mailing'),
        ),
    ]
