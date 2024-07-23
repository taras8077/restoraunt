from django.db import models

# Create your models here.

#category, dish


class Category(models.Model):
    name=models.CharField(max_length=255, verbose_name='назва')
    description=models.TextField(verbose_name='опис',blank=True,null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Категорія'
        verbose_name_plural='Категорії'
        ordering=['name']

class Dish(models.Model):
    name = models.CharField(max_length=255, verbose_name='назва')
    description = models.TextField(verbose_name='опис', blank=True, null=True)
    ingredients = models.TextField(verbose_name='Інгредієнти')
    photo = models.ImageField(upload_to='dish_images/', blank=True, null=True, verbose_name='Фото')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', verbose_name='категорія')
    is_available = models.BooleanField(default=True, verbose_name='В наявності')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Страва'
        verbose_name_plural='Страви'
        ordering=['category']
