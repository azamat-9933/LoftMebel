from django.shortcuts import render


def index(request):
    return render(request, 'loft/index.html')


def about(request):
    return render(request, 'loft/about.html')
