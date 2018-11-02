import random
from django.shortcuts import render
from goods.models import Goods, Category
from show.models import article, Class
from utils import all_show


def cate(request):
    cates = Category.objects.all()
    return render(request, 'index.html', locals())

def showall(request, cate_id):
    cates, essaies, all_class = all_show.all_show1(request)
    cate = Category.objects.get(id=cate_id)
    product_all = cate.goods_set.all()
    return render(request, 'product_list.html', locals())


def product_detail(request, product_id):
    cates, essaies, all_class = all_show.all_show1(request)
    product = Goods.objects.get(id=product_id)

    diffid_list = random.sample(range(1, 120), 4)
    diff_goods_all = map(lambda diffid: Goods.objects.get(id=diffid), diffid_list)

    diffid_list1 = random.sample(range(1, 120), 3)
    diff_goods_all1 = map(lambda diffid: Goods.objects.get(id=diffid), diffid_list1)

    bimgs = product.bigimg.bigPic.split('.jpg')
    bimg_list = [bimg+'.jpg' for bimg in bimgs][:-1]
    # bimg_list = []
    # for bimg in bimgs:
    #     bimg += '.jpg'
    #     bimg_list.append(bimg)
    # bimg_list = bimg_list[:-1]
    return render(request, 'single.html', locals())


