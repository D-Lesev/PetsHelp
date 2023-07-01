from django import forms
from .models import ItemShop


class ItemShopCreate(forms.ModelForm):
    class Meta:
        model = ItemShop
        fields = ['title', 'description', 'price', 'location', 'available_quantity', 'main_photo']
