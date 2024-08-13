from django.contrib.auth.models import User
from django.db import models

from menu.models import Dish


# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    created_at=models.DateTimeField(auto_now_add=True)
    is_ordered=models.BooleanField(default=False)
    class Meta:
        verbose_name='Кошик'
        verbose_name_plural='Кошики'
class Item_in_cart(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    dish=models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1, verbose_name='кількість')
    class Meta:
        verbose_name='Страва в кошику'
        verbose_name_plural='Страви в кошику'
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=255)
    total_price=models.DecimalField(decimal_places=2, max_digits=20)
    PAYMENT_CHOICES=(
        ('online', 'Онлайн оплата'),
        ('cash', 'Оплата готівкою при отриманні')
    )
    payment_method=models.CharField(max_length=255, choices=PAYMENT_CHOICES)
    status=models.CharField(max_length=255, default='new')
    comment=models.TextField(blank=True, null=True)
    class Meta:
        verbose_name='Замовлення'
        verbose_name_plural='Замовлення'