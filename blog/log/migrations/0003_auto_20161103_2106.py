# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-03 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
