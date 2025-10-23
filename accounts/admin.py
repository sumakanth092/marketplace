from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'is_staff', 'is_seller']
    list_filter = ['is_staff', 'is_seller', 'is_superuser']
    search_fields = ['username', 'email']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_seller',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_seller',)}),
    )
