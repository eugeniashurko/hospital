# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('histories', '0004_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='date_issued',
            field=models.DateField(default=datetime.date(2014, 11, 23), verbose_name='Date Issued'),
            preserve_default=False,
        ),
    ]
