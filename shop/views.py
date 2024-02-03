from django.shortcuts import render
from shop.models import Products


def shop(request):
    products = Products.objects.all()
    context = {
        'title': 'Shop home page',
        'products': products
    }
    return render(request, 'shop-sidebar-left.html', context)


def product(request, goods_slug):
    goods = Products.objects.get(slug=goods_slug)
    context = {
        'title': 'Single product',
        'goods': goods,
    }
    return render(request, 'shop-single.html', context)
