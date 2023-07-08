from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['phone', 'address', 'is_staff', 'is_active',
                    'profile_picture', 'age', 'pet_owner',
                    'first_name', 'last_name', 'email'
                    ]
    list_filter = ["pet_owner", "age"]
    search_fields = ["phone", "first_name"]
    ordering = ["first_name", "age", 'address']
