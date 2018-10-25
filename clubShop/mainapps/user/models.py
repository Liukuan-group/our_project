from django.contrib.auth.models import AbstractUser
from django.db import models
from db.base_model import BaseModel

# Create your models here.

class User(AbstractUser, BaseModel):
    '''继承于Django自带用户认证系统'''
    # def __str__(self):
    #     return self.username

    class Meta:
        db_table = 't_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Address(BaseModel):
    '''地址模型类'''
    user = models.ForeignKey('User', verbose_name='所属用户', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=50, verbose_name='收货地址')
    code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=15, verbose_name='手机号码')

    def __str__(self):
        return self.addr

    class Meta:
        db_table = 't_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name

