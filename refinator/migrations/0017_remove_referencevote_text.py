# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 04:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refinator', '0016_referencevote_vote_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referencevote',
            name='text',
        ),
    ]
