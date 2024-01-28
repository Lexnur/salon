from django.shortcuts import render


def landing(request):
    context = {
        'home': 'Hair salon - Home',

    }
    return render(request, 'landing.html', context)


def index(request):
    context = {
        'women': 'Hair salon - For women',
    }
    return render(request, 'index.html', context)


def index2(request): # Передать в context нужно только что-то одно
    context = {
        'men': 'Hair salon - For men',

    }
    return render(request, 'men.html', context)


def homepage3(request): # Передать в context нужно только что-то одно
    context = {
        'home': 'Hair salon - Home',
        'women': 'Hair salon - Women',
        'men': 'Hair salon - Men',
        'junior': 'Hair salon - Junior'

    }
    return render(request, 'homepage-3.html', context)

