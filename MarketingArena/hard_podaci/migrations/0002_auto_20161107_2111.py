# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hard_podaci', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ESN',
        ),
        migrations.DeleteModel(
            name='ESN_Sarajevo',
        ),
        migrations.DeleteModel(
            name='O_projektu',
        ),
    ]
