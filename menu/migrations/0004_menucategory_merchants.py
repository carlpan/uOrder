# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0001_initial'),
        ('menu', '0003_auto_20160108_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='menucategory',
            name='merchants',
            field=models.ManyToManyField(through='menu.MenuItem', to='merchants.Merchant'),
        ),
    ]
