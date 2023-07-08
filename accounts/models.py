from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    phone = models.CharField(max_length=15,
                             validators=[RegexValidator(regex=r'^\+\d{12}',
                                                        message='Phone must start with \'+\' and have 12 numbers')])
    address = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='accounts_picture/', blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    pet_owner = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
