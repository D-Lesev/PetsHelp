from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):

    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='accounts_picture/', blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    pet_owner = models.BooleanField(default=False)

