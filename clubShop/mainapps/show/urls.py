from django.conf.urls import url,include
from django.core.paginator import Paginator
from django.shortcuts import render
from show.views import product,content

from show.models import article


def products(request):
    essaies = article.objects.all()
    paginator = Paginator(essaies, per_page=8)
    page = paginator.page(request.GET.get('page', 1))
    return render(request, 'bikes.html', locals())



urlpatterns = [
    url(r'^articles/',products,name='articles'), #文章初始页
    url(r'^article/(\d+)/',product,name='article'), #文章页
    url(r'^content/(\d+)/',content,name='content'), #文章详情页
]
