from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # default is required=true

    # this is the configuration for the fields that we are going to add to our forms
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
