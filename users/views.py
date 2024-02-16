from django.shortcuts import render


def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'login.html', context)


def register(request):
    context = {
        'title': 'Registration',
    }
    return render(request, 'register.html', context)
