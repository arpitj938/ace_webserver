# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-19 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login_data',
            old_name='flag',
            new_name='content_flag',
        ),
        migrations.AddField(
            model_name='login_data',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='login_data',
            name='email_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='login_data',
            name='password',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
