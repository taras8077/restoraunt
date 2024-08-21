from django.contrib.auth.models import User
from django.db import models

from menu.models import Dish


# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', verbose_name='Клієнт')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    is_ordered=models.BooleanField(default=False, verbose_name='Замовлення')



    class Meta:
        verbose_name='Кошик'
        verbose_name_plural='Кошики'

    def __str__(self):
        return f'Кошик{self.pk} - {self.user} - {self.created_at}'


class Item_in_cart(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name='Кошик')
    dish=models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='Страва')
    quantity=models.IntegerField(default=1, verbose_name='кількість')


    class Meta:
        verbose_name='Страва в кошику'
        verbose_name_plural='Страви в кошику'

    def __str__(self):
        return f'Товар{self.dish} - Кількість {self.quantity}'


class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='Клієнт')
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='order', verbose_name='Кошик')
    phone_number=models.CharField(max_length=20, verbose_name='телефон')
    address=models.CharField(max_length=255,verbose_name='Адреса')
    total_price=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Ціна')
    PAYMENT_CHOICES=(
        ('online', 'Онлайн оплата'),
        ('cash', 'Оплата готівкою при отриманні')
    )
    payment_method=models.CharField(max_length=255, choices=PAYMENT_CHOICES, verbose_name='Спосіб оплати')
    status=models.CharField(max_length=255, default='new', verbose_name='Статус')
    comment=models.TextField(blank=True, null=True, verbose_name='Коментар')

    class Meta:
        verbose_name='Замовлення'
        verbose_name_plural='Замовлення'

    def __str__(self):
        return f'Замовлення №{self.pk} - {self.user}'