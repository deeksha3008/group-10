# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0004_temperature_moisture'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='ult_value',
            field=models.CharField(default=100, max_length=250),
            preserve_default=False,
        ),
    ]
