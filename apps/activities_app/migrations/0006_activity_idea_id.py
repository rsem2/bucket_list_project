# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-15 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities_app', '0005_auto_20180115_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='idea_id',
            field=models.IntegerField(null=True),
        ),
    ]
