# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_synchroniser', '0004_auto_20170611_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetnote',
            name='field',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='datasetnote',
            name='iati_identifier',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='datasetnote',
            name='message',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='datasetnote',
            name='model',
            field=models.CharField(max_length=255),
        ),
    ]