# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 10:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recurrence',
            new_name='Planner',
        ),
    ]
