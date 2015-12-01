# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0003_auto_20151130_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='trash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('messege', models.ForeignKey(related_name='msg', to='mymail.mailing')),
                ('receive', models.ForeignKey(related_name='receiv', to='mymail.mailing')),
                ('sender', models.ForeignKey(related_name='send', to='mymail.mailing')),
                ('subject', models.ForeignKey(related_name='sub', to='mymail.mailing')),
            ],
        ),
    ]
