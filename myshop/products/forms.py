from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Product


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter Username",
        "class": "form-control"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Enter Email",
        "class": "form-control"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter Password",
        "class": "form-control"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Repeat Password",
        "class": "form-control"
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter username",
        "class": "form-control",
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password",
        "class": "form-control",
    }))


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "price", "description", "image", "is_sold", "stock"]

        widgets = {
            "category": forms.Select(attrs={
                "placeholder": "Select Category",
                "class": "form-control",
            }),
            "name": forms.TextInput(attrs={
                "placeholder": "Product name",
                "class": "form-control",
            }),
            "price": forms.NumberInput(attrs={
                "placeholder": "Product price",
                "class": "form-control",
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Product description",
                "class": "form-control",
            }),
            "image": forms.FileInput(attrs={
                "class": "form-control",
            }),
            "stock": forms.TextInput(attrs={
                "placeholder": "Available stock quantity",
                "class": "form-control",
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "price", "description", "image", "is_sold", "stock"]

        widgets = {
            "category": forms.Select(attrs={
                "placeholder": "Select Category",
                "class": "form-control",
            }),
            "name": forms.TextInput(attrs={
                "placeholder": "Product name",
                "class": "form-control",
            }),
            "price": forms.TextInput(attrs={
                "placeholder": "Product price",
                "class": "form-control",
            }),
            "description": forms.TextInput(attrs={
                "placeholder": "Product description",
                "class": "form-control",
            }),
            "image": forms.FileInput(attrs={
                "class": "form-control",
            }),
            "stock": forms.TextInput(attrs={
                "placeholder": "Available stock quantity",
                "class": "form-control",
            }),
        }