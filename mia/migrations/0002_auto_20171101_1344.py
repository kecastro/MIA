# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-01 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='petsExtra',
            field=models.CharField(max_length=20, null=True),
        ),
    ]