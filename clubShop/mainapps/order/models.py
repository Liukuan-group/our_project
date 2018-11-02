from django.db import models
from db.base_model import BaseModel
from goods.models import Goods
from user.models import Address,User
# Create your models here.

class OrderInfo(BaseModel):
    '''订单信息模型类'''
    PAY_METHOD_CHOICES = (
        (1, '货到付款'),
        (2, '微信支付'),
        (3, '支付宝支付'),
        (4, '银联支付'),
    )
    ORDER_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成'),
    )
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name='地址', on_delete=models.CASCADE)
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='支付方式')
    price_total = models.FloatField(verbose_name='订单总价')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, verbose_name='订单状态')
    trade_no = models.CharField(max_length=128, verbose_name='支付编号')

    class Meta:
        db_table = 't_order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderDetail(models.Model):
    order = models.ForeignKey(OrderInfo,
                              on_delete=models.CASCADE,
                              verbose_name='订单')

    goods = models.ForeignKey(Goods,
                             on_delete=models.CASCADE,
                             verbose_name='小说')

    cnt = models.IntegerField(verbose_name='数量',
                              default=1)

    price = models.DecimalField(verbose_name='单价',
                                max_digits=10,
                                decimal_places=2)

    def __str__(self):
        return self.order.user + '的订单'

    class Meta:
        db_table = 't_order_detail'
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

