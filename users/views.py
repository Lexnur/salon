from django.shortcuts import render


def login(request):
    context = {
        'title': 'Авторизация',
    }
    return render(request, 'login.html', context)


def register(request):
    context = {
        'title': 'Регистрация',
    }
    return render(request, 'register.html', context)


def checkout(request):
    context = {
        'title': 'Оформление заказа',
    }
    return render(request, 'shop-checkout.html', context)


def shop_cart(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, 'shop-cart.html', context)


def logout(request):
    pass