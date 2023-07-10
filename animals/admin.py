from django.contrib import admin
from .models import AnimalAdoptReadyCreate, AnimalAtVetClinic


@admin.register(AnimalAdoptReadyCreate)
class AnimalAdoptReadyCreateAdmin(admin.ModelAdmin):
    list_display = ['animal_name', 'animal_type', 'location', 'user']
    raw_id_fields = ["user"]
    list_filter = ["animal_type", "location"]
    search_fields = ["animal_type", "location", 'user']
    ordering = ["animal_type", "location", 'user']


@admin.register(AnimalAtVetClinic)
class AnimalAtVetClinic(admin.ModelAdmin):
    list_display = ['type_animal', 'name_animal', 'vetclinic', 'vetclinic_city',
                    'current_bill', 'user']
    raw_id_fields = ["user"]
    list_filter = ["vetclinic", "vetclinic_city", 'current_bill', 'type_animal']
    search_fields = ["medical_record"]
    ordering = ["current_bill"]
