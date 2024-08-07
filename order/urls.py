from django.contrib import admin
from django.urls import path
from order import views

urlpatterns = [
    path('dish/<int:pk>/add-to-cart', views.AddToCartView.as_view(), name='add-to-cart'),
]
