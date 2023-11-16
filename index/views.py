from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def error404(request):
    return render(request, 'error404.html', {})

def error404_view(request, exception):
    return render(request, 'error404.html', {},status=404)
