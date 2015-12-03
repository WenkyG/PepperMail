# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymail', '0011_sent_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='sent_mai',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100)),
                ('messege', models.CharField(max_length=1000)),
                ('receive', models.ForeignKey(related_name='receiver', to='mymail.user')),
                ('sende', models.ForeignKey(related_name='sendr', to='mymail.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='sent_mail',
            name='receive',
        ),
        migrations.RemoveField(
            model_name='sent_mail',
            name='sende',
        ),
        migrations.DeleteModel(
            name='sent_mail',
        ),
    ]
