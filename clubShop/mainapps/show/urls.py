from django.conf.urls import url,include
from show.views import product,content





urlpatterns = [
    url(r'^article',product,name='article'), #文章页
    url(r'^content/(\d+)/',content,name='content'), #文章详情页
]
