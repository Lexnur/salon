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


def men(request): # Передать в context нужно только что-то одно
    context = {
        'men': 'Hair salon - For men',

    }
    return render(request, 'men.html', context)


def junior(request): # Передать в context нужно только что-то одно
    context = {
        'junior': 'Hair salon - Junior'
    }
    return render(request, 'junior.html', context)

