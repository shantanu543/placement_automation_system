# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-22 22:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0017_auto_20160422_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postgrad',
            old_name='yearofpassing',
            new_name='year_of_passing',
        ),
        migrations.RenameField(
            model_name='sec',
            old_name='yearofpassing',
            new_name='year_of_passing',
        ),
        migrations.RenameField(
            model_name='srsec',
            old_name='yearofpassing',
            new_name='year_of_passing',
        ),
        migrations.RenameField(
            model_name='undergrad',
            old_name='yearofpassing',
            new_name='year_of_passing',
        ),
    ]
