from django.contrib import admin

from menu.models import Category, Dish

# Register your models here.
admin.site.register(Dish)
admin.site.register(Category)
