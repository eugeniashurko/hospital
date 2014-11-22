# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20141121_2354'),
        ('histories', '0003_auto_20141122_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medicine', models.CharField(max_length=255, verbose_name='Medicine')),
                ('doctor', models.ForeignKey(to='profiles.Doctor')),
                ('medical_history', models.ForeignKey(to='histories.MedicalHistory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
