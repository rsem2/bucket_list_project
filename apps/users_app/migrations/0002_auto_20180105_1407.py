# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-05 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='users_app.User')),
                ('friend_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='users_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='friends_of', through='users_app.UserFriends', to='users_app.User'),
        ),
    ]