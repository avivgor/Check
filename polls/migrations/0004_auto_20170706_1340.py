# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 13:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170705_2022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citiesinsong',
            old_name='song_id',
            new_name='song',
        ),
    ]
