from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('<slug:category_slug>/', views.shop, name='shop'),
    path('<slug:category_slug>/<int:page>/', views.shop, name='shop'),
    path('product/<slug:goods_slug>/', views.product, name='product'),

]
