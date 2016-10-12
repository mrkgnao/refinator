# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 09:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('refinator', '0022_auto_20161011_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='added_by',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL), ),
        migrations.AddField(
            model_name='tag',
            name='added_date',
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False, ),
    ]