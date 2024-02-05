from django.shortcuts import render, get_list_or_404
from shop.models import Products


def shop(request, category_slug):
    if category_slug == 'all':
        products = Products.objects.all()
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    # products = Products.objects.all()
    context = {
        'title': 'Shop home page',
        'products': products,

    }
    return render(request, 'shop-sidebar-left.html', context)


def product(request, goods_slug):
    goods = Products.objects.get(slug=goods_slug)
    context = {
        'title': 'Single product',
        'goods': goods,
    }
    return render(request, 'shop-single.html', context)
