# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0002_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='case',
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='record',
            field=models.ForeignKey(to='histories.Record', null=True),
            preserve_default=True,
        ),
    ]
