# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unach_photo_server', '0004_auto_20170426_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photorepository',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='photorepository',
            name='database_column_filter',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='photorepository',
            name='database_column_search',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='photorepository',
            name='database_table_search',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]