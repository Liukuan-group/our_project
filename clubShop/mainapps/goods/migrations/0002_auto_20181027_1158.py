# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-27 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='desc',
            field=models.CharField(max_length=200, verbose_name='商品简介'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=50, verbose_name='商品名称'),
        ),
    ]
