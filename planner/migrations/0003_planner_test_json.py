# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 02:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20160427_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='planner',
            name='test_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
    ]