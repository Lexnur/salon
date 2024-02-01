from django.shortcuts import render


def shop(request):
    context = {
        'shop': 'Shop home page',
    }
    return render(request, 'shop-sidebar-left.html', context)


def product(request):
    context = {
        'product': 'Single product',
    }
    return render(request, 'shop-single.html', context)
