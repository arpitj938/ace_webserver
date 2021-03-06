# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-17 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20170217_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill_data',
            fields=[
                ('enroll_no', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('skill', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student_data',
            name='achivement',
        ),
        migrations.RemoveField(
            model_name='student_data',
            name='achivement_url',
        ),
        migrations.RemoveField(
            model_name='student_data',
            name='skill',
        ),
        migrations.AlterField(
            model_name='student_data',
            name='photo',
            field=models.ImageField(default='default.png', upload_to='student_images/'),
        ),
    ]
