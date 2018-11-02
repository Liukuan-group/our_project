from goods.models import Goods
from utils import redis_cache


def add_cart(user_id, goods_id, cnt=1):
    name = 'cart_%s'%user_id
    if redis_cache.hexists(name, goods_id):
        cnt += int(redis_cache.hget(name, goods_id).decode())

        #更新数量
    redis_cache.hset(name, goods_id, cnt)


def remove_cart(user_id, ids):
    # 判断goods_id是否在购物车
    name = 'cart_%s'%user_id
    for goods_id in ids:
        if redis_cache.hexists(name, goods_id):
            redis_cache.hdel(name, goods_id)

def count_cart(user_id):
    #同及当前用户下所有商品的和
    name = 'cart_%s'%user_id
    return sum([int(cnt.decode()) for goods_id,cnt in redis_cache.hgetall(name).items()])


def list_cart(user_id):
    name = 'cart_%s' % user_id
    goods = [(Goods.objects.get(id=id_.decode()),int(cnt.decode())) for id_, cnt in redis_cache.hgetall(name).items()]

    return goods

def get_cart_by_ids(user_id, ids):
    goods_list = list_cart(user_id)
    return [(goods, cnt) for goods, cnt in goods_list if goods.id in ids]