from django.conf.urls import url,include
from order.views import  goorder

urlpatterns = [
    url(r'^goorder/',goorder,name='test'),
    # url(r'^test/',test,name='test')
]
