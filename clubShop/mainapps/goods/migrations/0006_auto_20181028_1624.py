# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20181028_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smallimg',
            name='smallPic',
            field=models.ImageField(max_length=600, upload_to='', verbose_name='商品小图'),
        ),
    ]
