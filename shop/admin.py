from django.contrib import admin
from .models import ItemShop
# Register your models here.


@admin.register(ItemShop)
class ItemShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'location', 'available_quantity']
    raw_id_fields = ["user"]
    list_filter = ["price", 'location', 'available_quantity']
    search_fields = ["location", "title"]
    ordering = ["price", "location", 'available_quantity']

