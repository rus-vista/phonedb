# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-24 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0009_auto_20180124_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='externalnumber',
            name='customer',
        ),
        migrations.AlterField(
            model_name='internalnumber',
            name='type',
            field=models.CharField(choices=[('SKD', 'СКД'), ('MTT', 'МТТ'), ('MOA', 'МОА')], default='MTT', max_length=20),
        ),
    ]
