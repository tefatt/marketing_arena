# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hard_podaci', '0011_agenda_esn_sarajevo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kompanija',
            name='logo',
            field=models.ImageField(upload_to='Kompanija_Logo'),
        ),
        migrations.AlterField(
            model_name='trener',
            name='slika',
            field=models.ImageField(upload_to='Trener_Slike'),
        ),
        migrations.AlterField(
            model_name='trening',
            name='slika',
            field=models.ImageField(upload_to='Trening_Slike'),
        ),
    ]