import xadmin
from xadmin import views
from user.models import User, Address
from order.models import OrderInfo
from goods.models import Goods
from show.models import article, Class

# Register your models here.

class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GlobalSetting():
    site_title = 'Club管理后台'
    site_footer = '版权所有@三小只科技'

    # global_search_models = [article, Class]
    global_models_icon = {
        Address: 'glyphicon glyphicon-th-list',
        article: 'glyphicon glyphicon-bookmark',
        Class: 'glyphicon glyphicon-list-alt',
        Goods: 'glyphicon glyphicon-lock',
        OrderInfo: 'glyphicon glyphicon-yen'
    }

    apps_icons = {
        'show': 'glyphicon glyphicon-book'
    }


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


class UserAdmin():
    list_display = ['username', 'email']


class AddressAdmin():
    list_display = ['user', 'receiver', 'addr', 'phone']


class OrderInfoAdmin():
    list_display = ['user', 'address', 'pay_method','trade_no', 'price_total', 'order_status']


class GoodsAdmin():
    list_display = ['name', 'desc', 'price', 'image', 'status']


class ArticleAdmin():
    list_display = ['title', 'content', 'date', 'image']

    style_fields = {
        'info': 'ueditor'
    }

class ClassAdmin():
    list_display = ['name', 'desc', 'image', 'phone']
# xadmin.site.register(User, UserAdmin)
xadmin.site.register(Address, AddressAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(article, ArticleAdmin)
xadmin.site.register(Class, ClassAdmin)