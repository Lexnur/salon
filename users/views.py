from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from carts.models import Cart
from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('users:logouts'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('landing'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            return HttpResponseRedirect(reverse('landing'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Регистрация',
        'form': form
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


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('landing'))
