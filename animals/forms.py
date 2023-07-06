from django import forms
from .models import AnimalAdoptReadyCreate, AnimalAtVetClinic


class AnimalAdoptReadyForm(forms.ModelForm):
    class Meta:
        model = AnimalAdoptReadyCreate
        fields = ['animal_name', 'animal_type', 'location', 'details',
                  'other', 'picture']


class AnimalAdoptForm(forms.ModelForm):
    place_to_live = forms.CharField(max_length=50)
    # picture_of_place = forms.ImageField(upload_to='owner_homes/%Y/%m/%d/')
    other_pets = forms.CharField(widget=forms.Textarea)
    other_details = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = AnimalAdoptReadyCreate
        fields = [
            'animal_name', 'animal_type', 'location', 'details', 'other', 'picture',
        ]


class AnimalVetClinicCreateForm(forms.ModelForm):
    class Meta:
        model = AnimalAtVetClinic
        exclude = ['user']
        # fields = "__all__"
