from django import forms
from .models import AdoptPetModel, AdoptionHomeModel, ShareAnimalModel


class AdoptPetFormModel(forms.ModelForm):
    class Meta:
        model = AdoptPetModel
        fields = ["name_pet", "location", "pet_story", "photo", "date_of_adoption"]
        widgets = {
            "date_of_adoption": forms.DateInput(attrs={'type': 'date'})
        }


class AdoptionHomeCreateModel(forms.ModelForm):
    class Meta:
        model = AdoptionHomeModel
        fields = [
            'title',
            'province',
            'city',
            'picture',
            'animal_type',
            'description',
            'start_period',
            'end_period'
        ]
        widgets = {
            'start_period': forms.DateInput(attrs={'type': 'date'}),
            'end_period': forms.DateInput(attrs={'type': 'date'}),
        }


class ShareAnimalForm(forms.ModelForm):
    class Meta:
        model = ShareAnimalModel
        exclude = ['user']

        fields = [
            "title",
            "notes",
            "province",
            "city",
            "main_photo"
        ]

        widgets = {
            "province": forms.TextInput(attrs={'placeholder:': "Only",
                                               "class": "custom-share-img"}),
            "city": forms.TextInput(attrs={'placeholder:': "Only if there is no GPS geotagging in the picture",
                                           "class": "custom-share-img"}),
        }

        labels = {
            "main_photo": "Picture (if possible with geotagging)"
        }
