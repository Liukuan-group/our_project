from django.db import models
from db.base_model import BaseModel

# Create your models here.

class Class(BaseModel):
    name = models.CharField(max_length=20, verbose_name='课程名称')
    desc = models.CharField(max_length=100, verbose_name='课程描述')
    image = models.ImageField(upload_to='image/class', verbose_name='课程图片')
    phone = models.CharField(max_length=15, verbose_name='咨询电话')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_class'
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class article(BaseModel):
    '''文章模型类'''
    title = models.CharField(max_length=10, verbose_name='标题')
    content = models.TextField(max_length=200, verbose_name='内容')
    date = models.DateTimeField(null=True, verbose_name='日期')
    image = models.ImageField(upload_to='image/article', verbose_name='文章图片')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name