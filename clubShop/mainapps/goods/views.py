import json
import random
from django.shortcuts import render
from goods.models import Goods, Category
from show.models import article, Class


def cate(request):
    cates = Category.objects.all()
    # print(cates)
    return render(request, 'index.html', locals())

def showall(request, cate_id):
    cates = Category.objects.all()
    essaies = article.objects.all()
    all_class = Class.objects.all()
    cate = Category.objects.get(id=cate_id)
    product_all = cate.goods_set.all()
    # print(product_all)
    return render(request, 'product_list.html', locals())


def product_detail(request, product_id):
    cates = Category.objects.all()
    essaies = article.objects.all()
    all_class = Class.objects.all()
    product = Goods.objects.get(id=product_id)
    # product_cate = product.cate
    # product_all = Goods.objects.filter(cate_id=product_cate.id)
    # print(product_all)
    diffid_list = random.sample(range(1, 120), 4)
    diff_goods_all = map(lambda diffid: Goods.objects.get(id=diffid), diffid_list)

    diffid_list1 = random.sample(range(1, 120), 3)
    diff_goods_all1 = map(lambda diffid: Goods.objects.get(id=diffid), diffid_list1)

    bimgs = product.bigimg.bigPic.split('.jpg')
    # print(bimgs)
    # print(type(bimgs))
    bimg_list = []
    for bimg in bimgs:
        bimg += '.jpg'
        bimg_list.append(bimg)
    # print(bimg_list)
    bimg_list = bimg_list[:-1]
    return render(request, 'single.html', locals())


