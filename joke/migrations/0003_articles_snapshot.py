# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0002_auto_20161006_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='snapshot',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
