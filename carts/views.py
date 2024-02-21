from django.shortcuts import render, redirect

from carts.models import Cart
from shop.models import Products


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.first(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, product_slug):
    return render(request, '')


def cart_change(request, product_slug):
    return render(request, '')
