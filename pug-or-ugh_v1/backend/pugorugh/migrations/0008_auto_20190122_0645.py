# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-01-22 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pugorugh', '0007_auto_20190121_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdog',
            name='status',
            field=models.CharField(choices=[('l', 'Like'), ('d', 'Dislike'), ('u', 'Undecided')], max_length=2),
        ),
    ]
