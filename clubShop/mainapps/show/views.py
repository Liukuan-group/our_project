from django.shortcuts import render
from django.views.generic import View

from .models import article
# Create your views here.



def product(request):
    with open(r'F:\our_project\clubShop\mainapps\show\fitness.txt','r',encoding='utf8') as f:
        for i in f.readlines():
            a = eval(i)
            article.objects.create(title=a['title'],content=a['content'],image=a['picture'])
        f.close()
    essaies = article.objects.all()
    return render(request,'bikes.html',locals())
