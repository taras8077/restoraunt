from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from menu.models import Dish
from order.forms import AddToCartForm
from order.models import Item_in_cart, Cart


# Create your views here.

class AddToCartView(CreateView):
    model = Item_in_cart
    form_class = AddToCartForm

    def form_valid(self, form):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        dish = get_object_or_404(Dish, pk=self.kwargs['pk'])
        item, created = Item_in_cart.objects.get_or_create(cart=cart, dish=dish)
        item.quantity += form.cleaned_data['quantity']
        item.save()
        return redirect('dish-detail',pk=self.kwargs['pk'])