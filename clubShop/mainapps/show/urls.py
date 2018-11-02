from django.conf.urls import url,include
from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Category
from show.views import product, content, showclass, classdetail

from show.models import article, Class
from utils import all_show


def products(request):
    cates, essaies, all_class = all_show.all_show1(request)
    paginator = Paginator(essaies, per_page=8)
    page = paginator.page(request.GET.get('page', 1))
    return render(request, 'bikes.html', locals())

def classes(request):
    cates, essaies, all_class = all_show.all_show1(request)
    paginator = Paginator(all_class,per_page=8)
    page = paginator.page(request.GET.get('page',1))
    return render(request,'showclass.html',locals())




urlpatterns = [
    url(r'^articles/',products,name='articles'), #文章初始页
    url(r'^article/(\d+)/',product,name='article'), #文章页
    url(r'^content/(\d+)/',content,name='content'), #文章详情页
    url(r'^showclass/',classes,name='classes'), #课程首页
    url(r'^showclass/(\d+)',showclass,name='showclass'), #课程页
    url(r'^classdetail/(\d+)/',classdetail,name='classdetail') #课程详情页

]
