from django.db import models
from accounts.models import CustomUser
from PIL import Image

# Create your models here.


class AdoptPetModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    name_pet = models.CharField(max_length=30)
    location = models.CharField(max_length=50, blank=True)
    pet_story = models.TextField()
    photo = models.ImageField(upload_to='happy_adopted/')
    date_of_adoption = models.DateField()

    def __str__(self):
        return self.name_pet

    def save(self):
        super().save()

        img = Image.open(self.photo.path)

        if img.width > 640 or img.height > 480:
            new_img = (640, 480)
            img.thumbnail(new_img)
            img.save(self.photo.path)

