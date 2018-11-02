from django.shortcuts import render

from user.models import User, Address
from utils import all_show
from utils.cart import list_cart
from .models import OrderInfo


def goorder(request):
    cates, essaies, all_class = all_show.all_show1(request)
    # information = OrderInfo.objects.get(request.GET.get(id,'user'))
    username = request.session.get('user_login')
    user_id = User.objects.filter(username=username).first().id
    goods_price_cnt = list_cart(user_id)
    print(goods_price_cnt)
    total_price = sum([int(cnt)*goods.price for goods, cnt in goods_price_cnt ])
    address_list = Address.objects.filter(user_id=user_id).all()
    return render(request,"order.html",locals())

# def test(request):
#     addrs = ''
#     skus = ''
#     return render(request,'order.html',locals())