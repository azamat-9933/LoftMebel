from django.urls import path
from .views import index, about, contact, registration, favorites, basket, profile, product

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('registration/', registration, name='registration'),
    path('favorites/', favorites, name='favorites'),
    path('basket/', basket, name='basket'),
    path('profile/', profile, name='profile'),
    path('product/', product, name='product')
]
