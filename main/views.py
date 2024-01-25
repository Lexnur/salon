from django.shortcuts import render


def index(request): # Передать в context нужно только что-то одно
    context = {
        'home': 'Hair salon - Home',
        'women': 'Hair salon - Women',
        'men': 'Hair salon - Men',
        'junior': 'Hair salon - Junior'

    }
    return render(request, 'index.html', context)


def index2(request): # Передать в context нужно только что-то одно
    context = {
        'home': 'Hair salon - Home',
        'women': 'Hair salon - Women',
        'men': 'Hair salon - Men',
        'junior': 'Hair salon - Junior'

    }
    return render(request, 'index2.html', context)


def homepage3(request): # Передать в context нужно только что-то одно
    context = {
        'home': 'Hair salon - Home',
        'women': 'Hair salon - Women',
        'men': 'Hair salon - Men',
        'junior': 'Hair salon - Junior'

    }
    return render(request, 'homepage-3.html', context)

