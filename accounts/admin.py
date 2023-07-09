from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'phone', 'is_superuser', 'is_staff', 'is_active', 'created']
    list_filter = ["pet_owner", "age"]
    search_fields = ["phone", "first_name"]
    ordering = ["first_name", "age", 'address']
