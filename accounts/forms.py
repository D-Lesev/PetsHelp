from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):

        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            'phone',
            'address',
            'age',
            'profile_picture',
            'pet_owner',
        ]

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Your address'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Your current age'}),
            'pet_owner': forms.CheckboxInput(),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'profile-pic'}),
        }

        labels = {
            'username': 'Your desired username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Your Email',
            'phone': 'Your phone number',
            'address': 'Current address',
            'profile_picture': 'No files',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if email and CustomUser.objects.filter(email=email).exists():
            self.add_error('email', "This email cannot be used.")

        if username and CustomUser.objects.filter(username=username).exists():
            self.add_error('username', 'The username already exists.')

        return self.cleaned_data

    error_messages = {
        'password_mismatch': 'Passwords do not match'
    }
