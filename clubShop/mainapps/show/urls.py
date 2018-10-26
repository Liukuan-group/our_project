from django.conf.urls import url,include
from show.views import product


urlpatterns = [
    url(r'^article',product,name='article'), #登录
]
