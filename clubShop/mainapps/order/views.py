from django.shortcuts import render
from .models import OrderInfo


def order(request):
    information = OrderInfo.objects.get(request.GET.get(id,'user'))
    return render(request,"order.html",locals())

def test(request):
    addrs = ''
    skus = ''
    return render(request,'order.html',locals())