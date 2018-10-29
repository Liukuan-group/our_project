from django.db import models
from db.base_model import BaseModel
# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=30, verbose_name='分类名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_cate'
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Goods(BaseModel):
    '''商品模型类'''
    status_choices = (
        (0, '下线'),
        (1, '上线'),
    )
    name = models.CharField(max_length=50, verbose_name='商品名称')
    desc = models.CharField(max_length=200, verbose_name='商品简介')
    price = models.FloatField(verbose_name='商品价格')
    image = models.ImageField(upload_to='image/goods', verbose_name='商品图片')
    status = models.SmallIntegerField(choices=status_choices, verbose_name='商品状态')
    cate = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name


class smallImg(BaseModel):
    smallPic = models.CharField(verbose_name='商品小图', max_length=600)


    class Meta:
        db_table = 't_spic'
        verbose_name = '商品小图'
        verbose_name_plural = verbose_name


class bigImg(BaseModel):
    bigPic = models.CharField(verbose_name='商品大图', max_length=600)
    smallimg = models.OneToOneField('smallImg', on_delete=models.CASCADE, verbose_name='小图')
    product = models.OneToOneField('Goods', on_delete=models.CASCADE, verbose_name='商品')


    class Meta:
        db_table = 't_bpic'
        verbose_name = '商品大图'
        verbose_name_plural = verbose_name


