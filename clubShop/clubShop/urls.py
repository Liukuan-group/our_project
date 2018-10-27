"""clubShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import random

from django.conf.urls import url,include
from django.shortcuts import render

import xadmin as admin
from goods.models import Category, Goods
from show.models import article


def to_index(request):
    cates = Category.objects.all()
    essaies = article.objects.all()
    hid_list = random.sample(range(1592, 1650),6)
    hot_goods_all = map(lambda hid: Goods.objects.get(id=hid),hid_list)

    new_list = random.sample(range(1650, 1692), 6)
    new_goods_all = map(lambda nid: Goods.objects.get(id=nid), new_list)
    return render(request, 'index.html',locals())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^user/', include('user.urls', namespace='user')),#用户模块
    url(r'^goods/', include('goods.urls', namespace='goods')),
    url(r'^show/',include('show.urls',namespace='show')),  #文章展示模块
    url(r'^order/', include('order.urls', namespace='order')),
    url(r'', to_index),
]
