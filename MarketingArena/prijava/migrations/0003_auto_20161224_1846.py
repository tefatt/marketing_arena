# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-24 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prijava', '0002_auto_20161219_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aplikant',
            name='godina_rodjenja',
            field=models.DateField(default='24.12.2016'),
        ),
    ]
