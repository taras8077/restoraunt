from django.shortcuts import render
from django.views.generic import ListView

from menu.models import Dish


# Create your views here.

class MenuList(ListView):
    model = Dish
    context_object_name = "menu_list"
    template_name = "menu/menu_list.html"
    paginate_by = 10