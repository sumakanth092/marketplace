from django.urls import path
from . import views

urlpatterns = [
    # other urls
    path('profile/', views.profile, name='profile'),
]
