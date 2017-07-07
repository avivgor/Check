# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170706_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='citiesinsong',
            name='id',
            field=models.AutoField(db_column='cityId', default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='citiesinsong',
            name='city',
            field=models.CharField(db_column='city', max_length=200),
        ),
    ]
