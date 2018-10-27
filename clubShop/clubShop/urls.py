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
from django.conf.urls import url,include
from django.shortcuts import render

import xadmin as admin
from goods.models import Category


def to_index(request):
    cates = Category.objects.all()
    return render(request, 'index.html',locals())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^user/', include('user.urls', namespace='user')),#用户模块
    url(r'^goods/', include('goods.urls', namespace='goods')),
    url(r'^show/',include('show.urls',namespace='show')),  #文章展示模块
    url(r'', to_index),
]
