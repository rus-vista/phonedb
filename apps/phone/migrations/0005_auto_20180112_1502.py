# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-12 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0004_auto_20180112_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internalnumber',
            name='calling_line_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='phone.ExternalNumber'),
        ),
        migrations.AlterField(
            model_name='internalnumber',
            name='lan',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4'),
        ),
        migrations.AlterField(
            model_name='internalnumber',
            name='pass_device',
            field=models.CharField(max_length=20, verbose_name='Пароль устройства'),
        ),
    ]
