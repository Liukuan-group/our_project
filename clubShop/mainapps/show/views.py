from django.core.paginator import Paginator
from django.shortcuts import render


from .models import article
# Create your views here.

def product(request,pag):
    # with open(r'F:\our_project\clubShop\mainapps\show\fitness.txt','r',encoding='utf8') as f:
    #     for i in f.readlines():
    #         a = eval(i)
    #         article.objects.create(title=a['title'],content=a['content'],image=a['picture'])
    #     f.close()
    essaies = article.objects.all()
    paginator = Paginator(essaies, per_page=8)
    page = paginator.page(pag)
    return render(request,'bikes.html',locals())

def content(request,id):
    content_ = article.objects.get(id=id)
    essaies = article.objects.all()
    return render(request, 'article.html', locals())