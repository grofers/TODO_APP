# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('install_ts', models.DateTimeField(auto_now_add=True)),
                ('update_ts', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=512)),
                ('scheduled_date_time', models.DateTimeField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
