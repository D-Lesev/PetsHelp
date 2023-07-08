from django.db import models
from accounts.models import CustomUser
from django.core.validators import DecimalValidator, MinValueValidator
from .validators import check_for_letter, resize_file_image, image_count
from PIL import Image
from multiupload.fields import MultiImageField
from django.core.exceptions import ValidationError
# Create your models here.


class ItemShop(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, validators=[check_for_letter])
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.0)])
    location = models.CharField(max_length=200, blank=True)
    available_quantity = models.PositiveIntegerField()
    main_photo = models.ImageField(upload_to='item_images/')
    # pictures = MultiImageField(upload_to='item_images_additional/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.main_photo.path)

        if img.height > 480 or img.width > 640:
            new_img = (640, 480)
            img.thumbnail(new_img)
            img.save(self.main_photo.path)

    class Meta:
        verbose_name_plural = 'ItemShop'

            # def clean(self):
    #     max_pics = 5
    #
    #     # Custom validation for the pictures field
    #     if self.pictures.count() > max_pics:
    #         raise ValidationError("You can upload up to 5 images.")
