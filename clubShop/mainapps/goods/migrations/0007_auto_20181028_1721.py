# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_auto_20181028_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigimg',
            name='bigPic',
            field=models.CharField(max_length=600, verbose_name='商品大图'),
        ),
        migrations.AlterField(
            model_name='bigimg',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='smallimg',
            name='smallPic',
            field=models.CharField(max_length=600, verbose_name='商品小图'),
        ),
    ]
