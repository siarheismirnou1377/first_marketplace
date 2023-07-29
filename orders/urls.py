from django.urls import re_path
from . import views


app_name = "order"
urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
    re_path(r'^orders_user/$', views.orders, name='orders_user'),
]
