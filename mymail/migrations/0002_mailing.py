# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mailing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100)),
                ('messege', models.CharField(max_length=1000)),
                ('receiver', models.ForeignKey(related_name='receiver', to='mymail.user')),
                ('sender', models.ForeignKey(related_name='sender', to='mymail.user')),
            ],
        ),
    ]
