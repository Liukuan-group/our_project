from django.conf.urls import url, include

from user.views import RegisterView, LoginView, ActiveView

urlpatterns = [
    url(r'^register',RegisterView.as_view(),name='register'), #注册
    url(r'^login',LoginView.as_view(),name='login'), #登录
    url(r'^active',ActiveView.as_view(),name='active'), #激活

]