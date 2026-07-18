from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {
            "fields": ("phone", "role", "shop_name"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": ("phone", "role", "shop_name"),
        }),
    )

    list_display = (
        "username",
        "email",
        "role",
        "phone",
        "is_staff",
    )