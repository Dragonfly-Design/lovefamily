# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-28 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_auto_20180528_0307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='search_text',
            new_name='manual_search_text',
        ),
        migrations.AddField(
            model_name='page',
            name='ocr_search_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]