from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from orders.models import UserForJson


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']


class UserForJsonForm(forms.ModelForm):

    class Meta:
        model = UserForJson
        fields = ['username', 'password']
