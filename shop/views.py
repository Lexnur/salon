from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from shop.models import Products
from shop.utils import q_search


def shop(request, category_slug=None):
    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)
    if category_slug == 'all':  # Отображать главную страницу при slug == 'all'
        products = Products.objects.all()
    elif query:
        products = q_search(query)
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    paginator = Paginator(products, 3)  # Какое кол-во товаров отображать на каждой странице
    page = paginator.page(int(page))
    context = {
        'title': 'Shop home page',
        'products': page,
        'slug_url': category_slug,
    }
    return render(request, 'shop-sidebar-left.html', context)


def product(request, goods_slug):
    goods = Products.objects.get(slug=goods_slug)
    context = {
        'title': 'Single product',
        'goods': goods,
    }
    return render(request, 'shop-single.html', context=context)
