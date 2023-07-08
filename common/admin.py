from django.contrib import admin
from .models import AdoptPetModel, AdoptionHomeModel, ShareAnimalModel
# Register your models here.


@admin.register(AdoptPetModel)
class AdoptPetAdmin(admin.ModelAdmin):
    list_display = ['name_pet', 'location', 'date_of_adoption', 'user']
    raw_id_fields = ["user"]
    list_filter = ["date_of_adoption", "location"]
    search_fields = ["name_pet"]
    ordering = ["location", 'user']


@admin.register(AdoptionHomeModel)
class AdoptionHomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'city', 'animal_type', 'start_period', 'end_period']
    raw_id_fields = ["user"]
    list_filter = ["start_period", "city", 'animal_type']
    search_fields = ["city"]
    ordering = ["city", 'start_period', 'end_period']


@admin.register(ShareAnimalModel)
class ShareAnimalAdmin(admin.ModelAdmin):
    list_display = ['title', 'province', 'city', 'user']
    raw_id_fields = ["user"]
    list_filter = ["city"]
    search_fields = ["province", "city"]
    ordering = ["province", "city"]

