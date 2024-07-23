from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField("auth.Permission")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Роль користувача'
        verbose_name_plural='Ролі користувачів'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255, verbose_name='адреса', blank=True,null=True)
    phone = models.CharField(max_length=15,verbose_name='номер телефону',unique=True,blank=True,null=True)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name='Профіль користувача'
        verbose_name_plural='Профілі користувачів'