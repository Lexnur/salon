from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.shop, name='shop'),
    path('product/<slug:goods_slug>/', views.product, name='product'),
]
