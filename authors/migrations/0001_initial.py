# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=4)),
            ],
        ),
    ]
