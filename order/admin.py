from django.contrib import admin

from order.models import Cart, Item_in_cart, Order


class ItemCartInLine(admin.TabularInline):
    model = Item_in_cart
    extra = 0
    can_delete = False
    fields = ['dish', 'quantity']
    readonly_fields = ['dish', 'quantity']


class CartInLine(admin.StackedInline):
    model = Cart
    extra = 0
    can_delete = False
    fields = ['user']
    readonly_fields = ['user']
    inlines = [ItemCartInLine]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'payment_method', 'status', 'address',)
    list_display_links = ('id', 'user')
    list_editable = ('status', 'payment_method')
    #inlines = [ItemCartInLine]

# Register your models here.
admin.site.register(Cart)
admin.site.register(Item_in_cart)
admin.site.register(Order, OrderAdmin)