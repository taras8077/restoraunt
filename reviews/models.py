from django.contrib.auth.models import User
from django.db import models

from menu.models import Dish


# Create your models here.

class Review(models.Model):
    dish=models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField(blank=True, null=True)
    rating=models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=255, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Відгук'
        verbose_name_plural='Відгуки'
        ordering=['dish','created_at']