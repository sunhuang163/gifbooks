# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '分类'},
        ),
        migrations.RemoveField(
            model_name='articles',
            name='tag',
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=120, verbose_name='标题'),
        ),
    ]
