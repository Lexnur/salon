from django.shortcuts import render


def shop(request):
    context = {
        'title': 'Shop home page',
    }
    return render(request, 'shop-sidebar-left.html', context)


def product(request):
    context = {
        'title': 'Single product',
    }
    return render(request, 'shop-single.html', context)
