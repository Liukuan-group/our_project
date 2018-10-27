from django.conf.urls import url,include
from order.views import test

urlpatterns = [
    url(r'^test/',test,name='test')
]
