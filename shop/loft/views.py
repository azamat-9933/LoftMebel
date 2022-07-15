from django.shortcuts import render


def index(request):
    return render(request, 'loft/index.html')


def about(request):
    return render(request, 'loft/about.html')


def contact(request):
    return render(request, 'loft/contact.html')


def registration(request):
    return render(request, 'loft/registration.html')


def favorites(request):
    return render(request, 'loft/favorites.html')


def basket(request):
    return render(request, 'loft/basket.html')


def profile(request):
    return render(request, 'loft/profile.html')


def product(request):
    return render(request, 'loft/product.html')
