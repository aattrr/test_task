from django import forms
from orders.models import Order


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'customer', 'price']
