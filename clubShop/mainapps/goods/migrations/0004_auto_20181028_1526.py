# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20181028_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigimg',
            name='smallimg',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='goods.smallImg', verbose_name='小图'),
        ),
    ]
