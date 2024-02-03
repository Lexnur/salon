from django.shortcuts import render


def landing(request):
    context = {
        'title': 'Hair salon - Home',
    }
    return render(request, 'landing.html', context)


def index(request):
    context = {
        'title': 'Hair salon - For women',
    }
    return render(request, 'index.html', context)


def men(request):
    context = {
        'title': 'Hair salon - For men',
    }
    return render(request, 'men.html', context)


def junior(request):
    context = {
        'title': 'Hair salon - Junior'
    }
    return render(request, 'junior.html', context)

