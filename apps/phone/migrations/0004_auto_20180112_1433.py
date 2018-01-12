# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-12 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0003_auto_20180112_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_to_MG', models.CharField(choices=[('no', 'нет'), ('DTMF', 'донабор'), ('direct number', 'прямой номер')], default='no', max_length=20)),
                ('inner_number', models.CharField(max_length=10)),
                ('inner_number_passwd', models.CharField(max_length=20)),
                ('device', models.CharField(max_length=20)),
                ('login_device', models.CharField(max_length=20)),
                ('pass_device', models.CharField(max_length=20)),
                ('wan', models.GenericIPAddressField(protocol='IPv4')),
                ('lan', models.GenericIPAddressField(protocol='IPv4')),
                ('calling_line_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.ExternalNumber')),
            ],
        ),
        migrations.RemoveField(
            model_name='number',
            name='calling_line_id',
        ),
        migrations.RemoveField(
            model_name='client',
            name='access_to_MG',
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phone.InternalNumber'),
        ),
        migrations.DeleteModel(
            name='Number',
        ),
    ]