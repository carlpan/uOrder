# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.Merchant')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_name', models.CharField(max_length=128)),
                ('entry_description', models.CharField(max_length=200)),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('menu_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MenuCategory')),
            ],
        ),
    ]