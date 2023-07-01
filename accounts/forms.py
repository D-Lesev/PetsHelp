from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            'phone',
            'address',
            'age',
            'profile_picture',
            'pet_owner',
        )
