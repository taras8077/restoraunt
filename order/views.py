from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView

from menu.models import Dish
from order.forms import AddToCartForm, OrderSubmitForm
from order.models import Item_in_cart, Cart, Order


# Create your views here.

class AddToCartView(LoginRequiredMixin, FormView):
    form_class = AddToCartForm

    def get_active_cart(self):
        carts = Cart.objects.filter(user=self.request.user, is_ordered=False)
        if carts.exists():
            return carts.first()
        else:
            return  Cart.objects.create(user=self.request.user)

    def form_valid(self, form):
        cart = self.get_active_cart()
        dish = get_object_or_404(Dish, pk=self.kwargs['pk'])
        item, created = Item_in_cart.objects.get_or_create(cart=cart, dish=dish)
        item.quantity += form.cleaned_data['quantity']
        item.save()
        return redirect('dish-detail',pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy('dish-detail',pk=self.kwargs['pk'])


class CartDetail(LoginRequiredMixin, DetailView):
    model = Cart
    context_object_name = "cart"
    template_name = "order/cart.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.get_object()
        context['cart'] = cart
        return context

    def get_object(self):
        return Cart.objects.filter(user=self.request.user, is_ordered=False).first()


class CreateOrderView(LoginRequiredMixin, CreateView):
    template_name = "order/order_form.html"
    form_class = OrderSubmitForm
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user, is_ordered=False).first()
        context['cart'] = cart
        return context

    def form_valid(self, form):
        cart = Cart.objects.filter(user=self.request.user, is_ordered=False).first()
        cart.is_ordered = True
        cart.save()
        order = form.save(commit=False)
        order.cart=cart
        order.user=self.request.user
        order.total_price = sum(item.dish.price * item.quantity for item in cart.items.all())
        order.save()
        return redirect('menu-list')
