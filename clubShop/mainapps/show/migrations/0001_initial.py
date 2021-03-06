# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=10, verbose_name='标题')),
                ('content', models.TextField(max_length=200, verbose_name='内容')),
                ('date', models.DateTimeField(null=True, verbose_name='日期')),
                ('image', models.ImageField(upload_to='image/article', verbose_name='文章图片')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 't_article',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=20, verbose_name='课程名称')),
                ('desc', models.CharField(max_length=100, verbose_name='课程描述')),
                ('image', models.ImageField(upload_to='image/class', verbose_name='课程图片')),
                ('phone', models.CharField(max_length=15, verbose_name='咨询电话')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
                'db_table': 't_class',
            },
        ),
    ]
