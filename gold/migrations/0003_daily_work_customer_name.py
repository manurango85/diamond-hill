# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 11:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gold', '0002_auto_20160516_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='daily_work',
            name='customer_name',
            field=models.CharField(default=datetime.datetime(2016, 5, 16, 11, 26, 26, 294765, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]