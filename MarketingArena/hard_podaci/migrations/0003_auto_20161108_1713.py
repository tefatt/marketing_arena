# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hard_podaci', '0002_auto_20161107_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trener',
            old_name='ime_puno',
            new_name='ime_i_prezime',
        ),
        migrations.AddField(
            model_name='trener',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='trener',
            name='twitter',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]