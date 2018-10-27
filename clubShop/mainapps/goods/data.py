import json
from goods.models import Goods

product_dic = json.load(open(r'D:\test\git项目\our_project\clubShop\mainapps\goods\data8.json'))
print(type(product_dic[0]))
good = Goods()
good_name = product_dic[0]['商品名称'][0]
good_desc = product_dic[0]['商品介绍'][0]
good_price = product_dic[0]['商品价格'][0]
good_image = product_dic[0]['图片地址']
good.save()
