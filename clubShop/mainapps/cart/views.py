from django.http import JsonResponse
from django.shortcuts import render
from utils import all_show
from user.models import User
from utils import cart
# Create your views here.
def check_login(request):
    username = request.session.get('user_login')
    if not username:
        return JsonResponse({'code':100,'errmsg':'未登录'})
    return username


def add_cart(request, goods_id):
    # 判断用户是否登录
    username = check_login(request)
    user = User.objects.filter(username=username).first()
    user_id = user.id
    cart.add_cart(user_id, goods_id)

    cnt = cart.count_cart(user_id)
    request.session['cart_cnt'] = cnt
    return JsonResponse({'code':200,'msg':'添加成功'})

def cart_list(request):

    cates, essaies, all_class = all_show.all_show1(request)
    username = check_login(request)
    user = User.objects.filter(username=username).first()
    user_id = user.id
    goods_list = cart.list_cart(user_id)
    total_price = sum([good.price * cnt for good,cnt in goods_list])

    request.session['cart_cnt'] = cart.count_cart(user_id)
    print(request.session['cart_cnt'])

    return render(request, 'cart_list.html', locals())


def del_cart(request, goods_id):
    username = check_login(request)
    user = User.objects.filter(username=username).first()
    user_id = user.id

    cart.remove_cart(user_id, goods_id)

    # 更新购物车的总量
    request.session['cart_cnt'] = cart.count_cart(user_id)

    return JsonResponse({'code': 200,
                         'msg': '删除成功!'})



