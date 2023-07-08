from django.db import models
from django.utils.text import slugify
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

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.photo.path)

        if img.width > 640 or img.height > 480:
            new_img = (640, 480)
            img.thumbnail(new_img)
            img.save(self.photo.path)

    class Meta:
        verbose_name_plural = 'AdoptPet'


class AdoptionHomeModel(models.Model):
    animal_choice = {
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('other', 'Other')
    }

    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, editable=False)
    province = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    picture = models.ImageField(upload_to='adoption_homes/')
    animal_type = models.CharField(max_length=30, choices=animal_choice)
    description = models.TextField(blank=True)
    start_period = models.DateField()
    end_period = models.DateField(blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.pk}")

        super().save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.width > 640 or img.height > 480:
            new_img = (640, 480)
            img.thumbnail(new_img)
            img.save(self.picture.path)

    class Meta:
        verbose_name_plural = 'AdoptionHome'


class ShareAnimalModel(models.Model):
    title = models.CharField(max_length=40)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    notes = models.TextField(blank=True, null=True)
    province = models.CharField(max_length=30, default='Plovdiv')  # to delete default
    city = models.CharField(max_length=30, default='Plovdiv')  # to delete default
    main_photo = models.ImageField(upload_to='help_animals/%Y/%m/%d/')

    class Meta:
        verbose_name_plural = 'ShareAnimal'
