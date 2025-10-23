from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile_redirect, name='profile_redirect'),
]
