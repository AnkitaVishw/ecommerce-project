from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
            "role",
            "shop_name",
            "password1",
            "password2",

        ]

    def clean(self):
        cleaned_data = super().clean()

        role = cleaned_data.get("role")
        shop_name = cleaned_data.get("shop_name")

        if role == User.SELLER and not shop_name:
            self.add_error(
                "shop_name",
                "Shop name is required for sellers."
            )

        return cleaned_data
        cleaned_data = super().clean()

        role = cleaned_data.get("role")
        shop_name = cleaned_data.get("shop_name")

        if role == User.SELLER and not shop_name:
            self.add_error(
                "shop_name",
                "Shop name is required for sellers."
            )

        return cleaned_data
