from django.core.paginator import Paginator
from django.shortcuts import render
from goods.models import Category
# from goods.models import Category
from .models import article, Class


# Create your views here.

def product(request,pag):
    # with open(r'F:\our_project\clubShop\mainapps\show\fitness.txt','r',encoding='utf8') as f:
    #     for i in f.readlines():
    #         a = eval(i)
    #         article.objects.create(title=a['title'],content=a['content'],image=a['picture'])
    #     f.close()
    cates = Category.objects.all()
    essaies = article.objects.all()
    all_class = Class.objects.all()
    paginator = Paginator(essaies, per_page=8)
    page = paginator.page(pag)
    return render(request,'bikes.html',locals())

def content(request,id):
    cates = Category.objects.all()
    essaies = article.objects.all()
    all_class = Class.objects.all()
    content_ = article.objects.get(id=id)
    return render(request, 'article.html', locals())



def showclass(request,pag):
    cates = Category.objects.all()
    # print(cates)
    essaies = article.objects.all()
    all_class = Class.objects.all()
    paginator = Paginator(all_class,per_page=8)
    page = paginator.page(pag)
    return render(request,'showclass.html',locals())

def classdetail(request,id):
    cates = Category.objects.all()
    essaies = article.objects.all()
    all_class = Class.objects.all()
    classinfo = Class.objects.get(id=id)
    paginator = Paginator(all_class, per_page=8)
    page = paginator.page(request.GET.get('page',1))
    return render(request, 'classdetail.html', locals())
