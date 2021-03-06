# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-24 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0008_auto_20180122_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalnumber',
            name='internalnumber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phone.InternalNumber'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('1', 'Enabled'), ('0', 'Disabled')], default='0', max_length=10),
        ),
    ]
