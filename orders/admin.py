from django.contrib import admin
from .models import Customer, Order, UserForJson


class OrderInLine(admin.TabularInline):
    model = Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [OrderInLine]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'customer', 'price']


@admin.register(UserForJson)
class UserForJsonAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']
