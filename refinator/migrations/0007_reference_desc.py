# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refinator', '0006_auto_20161008_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='desc',
            field=models.CharField(default='', max_length=5000),
        ),
    ]