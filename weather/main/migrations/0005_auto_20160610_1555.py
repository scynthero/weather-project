# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160610_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
