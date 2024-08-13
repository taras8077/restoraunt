from django.shortcuts import render
from django.views.generic import ListView, DetailView

from menu.models import Dish, Category
from order.forms import AddToCartForm


# Create your views here.

class MenuList(ListView):
    model = Dish
    context_object_name = "menu_list"
    template_name = "menu/menu_list.html"
    # paginate_by = 10


class CategoryList(DetailView):
    model = Category
    context_object_name = "category_list"
    template_name = 'menu/category_list.html'


class DishDetailView(DetailView):
    model = Dish
    context_object_name = "dish"
    template_name = 'menu/dish_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DishDetailView, self).get_context_data()
        context['addForm'] = AddToCartForm()
        return context