# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-22 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160922_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publisher_date',
        ),
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
    ]
