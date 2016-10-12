# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 03:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [('refinator', '0013_auto_20161009_0348'), ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='speaker',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL), ),
    ]
