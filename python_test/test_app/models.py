from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    date_of_birth = models.DateTimeField(null=True)
    date_of_registration = models.DateTimeField(null=True)
    order = models.ForeignKey('Order',on_delete=models.CASCADE,null=True,verbose_name='order')
    class Meta:
        verbose_name_plural = "users"
        verbose_name = 'user'
    def __str__(self):
        return self.username

class Order(models.Model):
    date_of_creation = models.DateTimeField(auto_now=True)
    goods = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "orders"
        verbose_name = 'order'
    def __str__(self):
        return self.goods