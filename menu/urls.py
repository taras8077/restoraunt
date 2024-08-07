from django.contrib import admin
from django.urls import path

from menu import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='menu-list'),
    path('category/<int:pk>', views.CategoryList.as_view(), name='category-list'),
    path('dish/<int:pk>', views.DishDetailView.as_view(), name='dish-detail'),
]
