from django.db import models

# Create your models here.

#category, dish


class Category(models.Model):
    name=models.CharField(max_length=255, verbose_name='назва')
    description=models.TextField(verbose_name='опис',blank=True,null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255, verbose_name='назва')
    description = models.TextField(verbose_name='опис', blank=True, null=True)
    ingredients = models.TextField(verbose_name='Інгредієнти')
    photo = models.ImageField(upload_to='dish_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
