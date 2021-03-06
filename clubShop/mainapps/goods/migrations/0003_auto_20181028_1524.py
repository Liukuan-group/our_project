# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20181027_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='bigImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('bigPic', models.ImageField(max_length=200, upload_to='', verbose_name='商品大图')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品大图',
                'verbose_name_plural': '商品大图',
                'db_table': 't_bpic',
            },
        ),
        migrations.CreateModel(
            name='smallImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('smallPic', models.ImageField(max_length=200, upload_to='', verbose_name='商品小图')),
            ],
            options={
                'verbose_name': '商品小图',
                'verbose_name_plural': '商品小图',
                'db_table': 't_spic',
            },
        ),
        migrations.AddField(
            model_name='bigimg',
            name='smallimg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.smallImg', verbose_name='小图'),
        ),
    ]
