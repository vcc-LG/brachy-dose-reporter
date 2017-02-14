# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fraction_number', models.IntegerField()),
                ('D90', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='fraction',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doseapp.Patient'),
        ),
    ]
