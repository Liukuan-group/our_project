from django.conf.urls import url
from cart.views import add_cart, cart_list, del_cart

urlpatterns = [
    url(r'^add/(\d+)/',add_cart, name='add_cart'),
    url(r'^go_cart/',cart_list,name='go_cart'),
    url(r'^del/(\d+)/', del_cart, name='del_cart'),
]
