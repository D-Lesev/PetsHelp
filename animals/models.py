from django.db import models
from django.core.validators import MinLengthValidator
from accounts.models import CustomUser


class AnimalAdoptReadyCreate(models.Model):
    animal_choice = {
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('other', 'Other')
    }

    animal_name = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    animal_type = models.CharField(max_length=30, choices=animal_choice)
    location = models.CharField(max_length=40, validators=[MinLengthValidator(2)])
    details = models.TextField()
    other = models.TextField(blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pets_for_adoption/')

    class Meta:
        verbose_name_plural = 'AnimalAdoptReady'

    def __str__(self):
        return self.animal_name


class AnimalAtVetClinic(models.Model):

    animal_type = {
        ('dog', "Dog"),
        ('cat', 'Cat'),
        ('other', 'Other')
    }

    type_animal = models.CharField(max_length=20, choices=animal_type)
    name_animal = models.CharField(max_length=30, validators=[MinLengthValidator(2)])
    medical_record = models.TextField()
    vetclinic = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    vetclinic_city = models.CharField(max_length=40, validators=[MinLengthValidator(2)])
    details_pet = models.TextField(blank=True, null=True)
    current_bill = models.FloatField()
    pictures = models.ImageField(upload_to='vetclinic/%Y/%m/%d/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'AnimalVetClinic'

    def __str__(self):
        return self.name_animal
