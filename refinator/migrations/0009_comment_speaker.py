# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('refinator', '0008_auto_20161008_0756'), ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='speaker',
            field=models.CharField(
                default='', max_length=200),
            preserve_default=False, ),
    ]
