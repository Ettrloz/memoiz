from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Informasi Tambahan", {"fields": ("no_telepon", "alamat")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Informasi Tambahan", {"fields": ("no_telepon", "alamat")}),
    )
    list_display = ("username", "email", "no_telepon", "is_staff")
