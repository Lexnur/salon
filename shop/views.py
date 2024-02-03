from django.shortcuts import render
from shop.models import Products


def shop(request):
    products = Products.objects.all()
    context = {
        'title': 'Shop home page',
        'products': products
    }
    return render(request, 'shop-sidebar-left.html', context)


def product(request):
    context = {
        'title': 'Single product',
    }
    return render(request, 'shop-single.html', context)
