# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refinator', '0017_remove_referencevote_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('tag_slug',)},
        ),
        migrations.RemoveField(
            model_name='reference',
            name='followups',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='prereqs',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='read_with',
        ),
    ]
