from PIL import Image
from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import CustomUser
from .validators import check_for_letter


def get_user_item_folder(instance, image):
    user_pk = instance.user.pk
    return f'item_images/{user_pk}/{image}'


class ItemShop(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, validators=[check_for_letter])
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.0)])
    location = models.CharField(max_length=50, blank=True)
    available_quantity = models.PositiveIntegerField()
    main_photo = models.ImageField(upload_to=get_user_item_folder)
    created = models.DateTimeField(auto_now_add=True)

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
        ordering = ['-created']
