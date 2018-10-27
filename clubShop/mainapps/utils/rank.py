# from utils import redis_cache
# from goods.models import Goods
#
#
# def add_day_rank(good_id):
#     flag = redis_cache.exists('DayRank')
#     redis_cache.zincrby('DayRank', good_id)
#