from django.db import models

from accounts.models import CustomUser

# Create your models here.


class AnimalAdoptReadyCreate(models.Model):
    animal_choice = {
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('other', 'Other')
    }

    animal_name = models.CharField(max_length=20)
    animal_type = models.CharField(max_length=30, choices=animal_choice)
    location = models.CharField(max_length=60)
    details = models.TextField()
    other = models.TextField(blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pets_for_adoption/')

    def __str__(self):
        return self.animal_name

