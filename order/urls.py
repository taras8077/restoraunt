from django.contrib import admin
from django.urls import path
from order import views

urlpatterns = [
    path('dish/<int:pk>/add-to-cart', views.AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', views.CartDetail.as_view(), name='cart-detail'),
    path('create/', views.CreateOrderView.as_view(), name='order-create'),

]
