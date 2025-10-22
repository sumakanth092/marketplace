from django.urls import path
from . import views

urlpatterns = [
    path('accounts/profile/', views.profile_redirect, name='profile_redirect'),
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
]
