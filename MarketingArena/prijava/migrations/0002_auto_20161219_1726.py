# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prijava', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aplikant',
            name='cv',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='dizajn_iskustvo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='drzanje_govora_iskustvo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='fakultet',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='godina_fakulteta',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='motivaciono_pismo',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='nvo_iskustvo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='opis_dizajn_iskustvo',
            field=models.TextField(default=None, max_length=800),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='opis_drzanje_govora_iskustvo',
            field=models.TextField(default=None, max_length=800),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='opis_nvo_iskustvo',
            field=models.TextField(default=None, max_length=800),
        ),
        migrations.AddField(
            model_name='aplikant',
            name='slika',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='aplikant',
            name='godina_rodjenja',
            field=models.DateField(default=None),
        ),
    ]