# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-01-21 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0004_auto_20190121_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpref',
            name='age',
            field=models.CharField(default='b,y,a,s', max_length=10),
        ),
    ]
