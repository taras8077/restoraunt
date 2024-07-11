from django.contrib import admin

from order.models import Cart, Item_in_cart, Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(Item_in_cart)
admin.site.register(Order)