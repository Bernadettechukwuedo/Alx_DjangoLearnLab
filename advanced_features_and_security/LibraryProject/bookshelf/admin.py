from django.contrib import admin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = [
        "email",
        "date_of_birth",
        "profile_photo",
        "is_staff",
        "is_superuser",
        "username",
    ]
    search_fields = ["email"]
    list_filter = ["date_of_birth"]


admin.site.register(CustomUser, CustomUserAdmin)
