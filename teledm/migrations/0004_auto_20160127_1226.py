# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teledm', '0003_auto_20160127_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='idcountry',
            new_name='country_id',
        ),
        migrations.RenameField(
            model_name='station',
            old_name='idstation',
            new_name='station_id',
        ),
    ]