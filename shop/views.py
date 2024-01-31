from django.shortcuts import render


def shop(request):
    context = {
        'shop': 'Shop',
    }
    return render(request, 'shop-sidebar-left.html', context)


def product(request):
    context = {
        'catalog': 'Catalog',
    }
    return render(request, 'shop-single.html', context)
