# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0001_initial'),
        ('menu', '0004_menucategory_merchants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menucategory',
            name='merchants',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='merchant',
        ),
        migrations.AddField(
            model_name='menucategory',
            name='merchant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='merchants.Merchant'),
        ),
    ]
