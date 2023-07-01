from django.db import models
from accounts.models import CustomUser
from django.core.validators import DecimalValidator, MinValueValidator
from .validators import check_for_letter, resize_file_image, image_count
from multiupload.fields import MultiImageField
from django.core.exceptions import ValidationError
# Create your models here.


class ItemShop(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, validators=[check_for_letter])
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.0), DecimalValidator])
    location = models.CharField(max_length=200, blank=True)
    available_quantity = models.PositiveIntegerField()
    main_photo = models.ImageField(upload_to='item_images/', validators=[resize_file_image])
    # pictures = MultiImageField(upload_to='item_images_additional/')

    def __str__(self):
        return self.title

    # def clean(self):
    #     max_pics = 5
    #
    #     # Custom validation for the pictures field
    #     if self.pictures.count() > max_pics:
    #         raise ValidationError("You can upload up to 5 images.")
