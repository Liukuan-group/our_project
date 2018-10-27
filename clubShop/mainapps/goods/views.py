import json
import random

from django.shortcuts import render
from goods.models import Goods, Category
# Create your views here.


# with open('D:\test\git项目\our_project\clubShop\mainapps\goods\data8.json','r') as f:
#     product_dic = json.dumps(f)
#     for
# product_dic = json.loads(open(r'D:\test\git项目\our_project\clubShop\mainapps\goods\data8.json'))
# good = Goods()
# good.name = product_dic[0]['商品名称'][0]
# good.desc = product_dic[0]['商品介绍'][0]
# good.price = product_dic[0]['商品价格'][0]
# good.image = product_dic[0]['图片地址']
# good.save()
from show.models import article


def cate(request):
    cates = Category.objects.all()
    print(cates)
    return render(request, 'index.html', locals())

def showall(request, cate_id):
    cates = Category.objects.all()
    essaies = article.objects.all()
    cate = Category.objects.get(id=cate_id)
    product_all = cate.goods_set.all()
    print(product_all)
    return render(request, 'product_list.html', locals())

# def hot_goods(request):
#     hot_goods_all = Goods.objects.raw('select * from t_goods order by id where id > 7')
#     print(hot_goods_all)
#     return render(request, 'index.html', locals())


def product_detail(request, product_id):
    cates = Category.objects.all()

    essaies = article.objects.all()
    product = Goods.objects.get(id=product_id)
    return render(request, 'single.html', locals())


