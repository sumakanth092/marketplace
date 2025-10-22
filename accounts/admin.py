from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # if you have a custom user model
admin.site.register(CustomUser, UserAdmin)
