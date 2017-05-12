# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import unach_photo_server.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('token', models.CharField(default=unach_photo_server.models.generate_hash, editable=False, max_length=40, unique=True)),
                ('domain_name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('repo_type', models.CharField(choices=[('file_system', 'File System'), ('database', 'Database')], max_length=20)),
                ('user_id', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=80, null=True)),
                ('client_machine_name', models.CharField(blank=True, max_length=255, null=True)),
                ('server_name', models.CharField(blank=True, max_length=255, null=True)),
                ('domain', models.CharField(blank=True, max_length=100, null=True)),
                ('server_ip', models.CharField(blank=True, max_length=100, null=True)),
                ('engine', models.CharField(blank=True, choices=[('postgres', 'Postgres'), ('mysql', 'Mysql'), ('oracle', 'Oracle')], max_length=10, null=True)),
                ('database_name', models.CharField(blank=True, max_length=50, null=True)),
                ('database_user', models.CharField(blank=True, max_length=50, null=True)),
                ('database_password', models.CharField(blank=True, max_length=80, null=True)),
                ('database_host', models.CharField(blank=True, max_length=100, null=True)),
                ('database_port', models.CharField(blank=True, max_length=10, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
