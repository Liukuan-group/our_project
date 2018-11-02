from django.core.paginator import Paginator
from django.shortcuts import render
from goods.models import Category
# from goods.models import Category
from utils import all_show
from .models import article, Class


# Create your views here.

def product(request,pag):

    cates, essaies, all_class = all_show.all_show1(request)
    paginator = Paginator(essaies, per_page=8)
    page = paginator.page(pag)
    return render(request,'bikes.html',locals())

def content(request,id):
    cates, essaies, all_class = all_show.all_show1(request)
    content_ = article.objects.get(id=id)
    return render(request, 'article.html', locals())



def showclass(request,pag):
    cates, essaies, all_class = all_show.all_show1(request)
    paginator = Paginator(all_class,per_page=8)
    page = paginator.page(pag)
    return render(request,'showclass.html',locals())

def classdetail(request,id):
    cates, essaies, all_class = all_show.all_show1(request)
    classinfo = Class.objects.get(id=id)
    paginator = Paginator(all_class, per_page=8)
    page = paginator.page(request.GET.get('page',1))
    return render(request, 'classdetail.html', locals())
