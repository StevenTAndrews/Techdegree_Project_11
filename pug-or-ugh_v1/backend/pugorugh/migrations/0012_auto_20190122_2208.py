# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-01-22 22:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0011_auto_20190122_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdog',
            old_name='decision',
            new_name='status',
        ),
    ]
