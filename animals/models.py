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


class AnimalAtVetClinic(models.Model):

    animal_type = {
        ('dog', "Dog"),
        ('cat', 'Cat'),
        ('other', 'Other')
    }

    type_animal = models.CharField(max_length=20, choices=animal_type)
    name_animal = models.CharField(max_length=30)
    medical_record = models.TextField()
    vetclinic = models.CharField(max_length=50)
    vetclinic_city = models.CharField(max_length=40)
    details_pet = models.TextField(blank=True, null=True)
    current_bill = models.FloatField()
    pictures = models.ImageField(upload_to='vetclinic/%Y/%m/%d/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

