from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('shop-cart/', views.shop_cart, name='shop_cart'),

]
