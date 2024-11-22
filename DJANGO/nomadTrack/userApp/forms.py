from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="",
    )
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text="",
    )
    username = forms.CharField(
        max_length=150,
        help_text="",
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="",
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="",
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")
