# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-17 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty_data',
            name='photo',
            field=models.ImageField(default='media/default.png', upload_to='media/faculty_images/'),
        ),
    ]
