# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratoryTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('date_taken', models.DateField(verbose_name='Date Taken')),
                ('place_taken', models.CharField(max_length=255, verbose_name='Place Taken')),
                ('date_measured', models.DateField(verbose_name='Date Measured')),
                ('results', models.TextField(verbose_name='Results')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedicalCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_issued', models.DateField(null=True, verbose_name='Date Issued', blank=True)),
            ],
            options={
                'ordering': ('date_issued',),
                'verbose_name': 'Medical Card',
                'verbose_name_plural': 'Medical Cards',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preliminary_diagnosis', models.CharField(max_length=255, verbose_name='Preliminary Diagnosis')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(null=True, verbose_name='End Date', blank=True)),
                ('complaints', models.TextField(verbose_name='Complaints')),
                ('anamnesis', models.TextField(null=True, verbose_name='Anamnesis', blank=True)),
                ('objective_examination', models.TextField(null=True, verbose_name='Objective Examination', blank=True)),
                ('final_diagnosis', models.CharField(max_length=255, null=True, verbose_name='Final Diagnosis', blank=True)),
                ('associated_disease', models.CharField(max_length=255, null=True, verbose_name='Associated Disease', blank=True)),
                ('complications', models.TextField(null=True, verbose_name='Complications', blank=True)),
                ('treatment_plan', models.TextField(null=True, verbose_name='Treatment Plan', blank=True)),
                ('doctor', models.ForeignKey(related_query_name=b'Medical History', related_name=b'Medical History', blank=True, to='profiles.Doctor', null=True)),
                ('medical_card', models.OneToOneField(to='histories.MedicalCard')),
            ],
            options={
                'ordering': ('start_date',),
                'verbose_name': 'Medical History',
                'verbose_name_plural': 'Medical Histories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Date of birth', blank=True)),
                ('telephone', models.CharField(max_length=255, null=True, verbose_name='Telephone', blank=True)),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Address', blank=True)),
                ('occupation', models.CharField(max_length=255, null=True, verbose_name='Occupation', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='medicalcard',
            name='patient',
            field=models.ForeignKey(to='histories.Patient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='laboratorytest',
            name='medical_history',
            field=models.OneToOneField(to='histories.MedicalHistory'),
            preserve_default=True,
        ),
    ]
