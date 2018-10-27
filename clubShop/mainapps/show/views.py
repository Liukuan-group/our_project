from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View

from .models import article
# Create your views here.



def product(request):
    # with open(r'D:\test\git项目\our_project\clubShop\mainapps\show\fitness.txt','r',encoding='utf8') as f:
    #     for i in f.readlines():
    #         a = eval(i)
    #         article.objects.create(title=a['title'],content=a['content'],image=a['picture'])
    #     f.close()
    essaies = article.objects.all()
    paginator = Paginator(essaies, per_page=8)
    pager = paginator.page(request.GET.get('page', 1))
    return render(request,'bikes.html',locals())

def content(request,id):
    content_ = article.objects.get(id=id)
    return render(request,'article.html',locals())