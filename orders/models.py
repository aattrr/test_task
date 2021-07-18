from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Customer(models.Model):
    """ Модель заказчик """
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """ Модель заказа """
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={"pk": self.pk})


class UserForJson(models.Model):
    """ Модель суперпользователя """
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
