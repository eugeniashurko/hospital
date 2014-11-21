# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Date of birth', blank=True)),
                ('telephone', models.CharField(max_length=255, verbose_name='Telephone')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('head_of_department', models.BooleanField(default=False, verbose_name='Head of Department?')),
                ('department', models.ForeignKey(to='administration.Department')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Date of birth', blank=True)),
                ('telephone', models.CharField(max_length=255, verbose_name='Telephone')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Nurse',
                'verbose_name_plural': 'Nurses',
            },
            bases=(models.Model,),
        ),
    ]
