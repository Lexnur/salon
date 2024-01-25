from django.shortcuts import render


def index(request):
    context = {
        'title': 'Hair salon'
    }
    return render(request, 'index.html', context)

