from django import forms
from .models import AnimalAdoptReadyCreate


class AnimalAdoptReadyForm(forms.ModelForm):
    class Meta:
        model = AnimalAdoptReadyCreate
        fields = ['animal_name', 'animal_type', 'location', 'details',
                  'other', 'picture']
