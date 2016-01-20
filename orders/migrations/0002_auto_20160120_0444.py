# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 04:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20160108_0302'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.MenuItem')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='arrival_time',
            field=models.TimeField(blank=True, choices=[(1, '10'), (2, '15'), (3, '20')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='current_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
    ]
