# from django.contrib.auth.models import AbstractUser, User
# from django.db import models
#
#
# class Category(models.Model):
#     title = models.CharField(max_length=30, verbose_name='Название')
#     icon = models.ImageField(upload_to='photo/category_icon', verbose_name='Иконка')
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.title
#
#
# class Company(models.Model):
#     title = models.CharField(max_length=30, verbose_name='Название')
#     icon = models.ImageField(upload_to='photo/company_icon', verbose_name='Иконка')
#
#
# class Product(models.Model):
#     title = models.CharField(max_length=50, verbose_name='Название')
#     description = models.CharField(max_length=150, verbose_name='Описание')
#     price = models.IntegerField(verbose_name='Цена')
#     company_name = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания')
#     width = models.IntegerField(verbose_name='Ширина')
#     depth = models.IntegerField(verbose_name='Глубина')
#     height = models.IntegerField(verbose_name='Высота')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
#
#     class Meta:
#         verbose_name = 'Мебель'
#         verbose_name_plural = 'Мебели'
#
#     def __str__(self):
#         return self.title
#
#
# class LoftUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
# # class Color(models.Model):
# #     color = models.CharField(max_length=10, verbose_name='Цвет')
# #     product = models.ForeignKey(Product, on_delete=models.)
