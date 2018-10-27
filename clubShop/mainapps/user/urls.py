from django.conf.urls import url

from user.views import RegisterView, LoginView,log_out,AddressView,showaddress





urlpatterns = [
    url(r'^register/',RegisterView.as_view(),name='register'), #注册
    url(r'^login/',LoginView.as_view(),name='login'), #登录
    url(r'^logout/',log_out,name='logout'), #退出登录
    url(r'^address/(?P<name>.+)/',showaddress,name='address'), #收货地址
    url(r'^add/(?P<name>.+)/',AddressView.as_view(),name='add'), #添加收货地址

]