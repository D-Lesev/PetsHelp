from django import forms
from .models import AdoptPetModel


class AdoptPetFormModel(forms.ModelForm):
    class Meta:
        model = AdoptPetModel
        fields = ["name_pet", "location", "pet_story", "photo", "date_of_adoption"]
        widgets = {
            "date_of_adoption": forms.DateInput(attrs={'type': 'date'})
        }
