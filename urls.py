from django.contrib import admin
from django.urls import path
from . import views
#from online_store import views as user_view
from django.contrib.auth import views as auth



urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('detail', views.detail, name='detail'),
    path('shop', views.shop, name='shop'),
    path('contact', views.contact, name='contact'),
]