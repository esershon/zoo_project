# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-19 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg_app', '0002_remove_users_user_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='desc',
        ),
        migrations.AddField(
            model_name='users',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='users',
            name='money',
            field=models.IntegerField(default=50000),
        ),
    ]