# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-03 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=10)),
                ('time', models.DateTimeField()),
                ('text', models.TextField()),
                ('discuss', models.CharField(max_length=120)),
            ],
        ),
    ]
