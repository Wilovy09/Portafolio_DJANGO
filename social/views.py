from django.shortcuts import render

def social(request):
    return render(request, 'social.html', {})
