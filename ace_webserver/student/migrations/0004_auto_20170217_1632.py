# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-17 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20170217_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='photo',
            field=models.ImageField(default='/media/default.png', upload_to='media/student_images/'),
        ),
    ]
