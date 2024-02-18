from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('landing'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form,
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