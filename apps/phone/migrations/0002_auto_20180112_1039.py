# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-12 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
