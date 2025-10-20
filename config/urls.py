from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Default app
    path('accounts/', include('accounts.urls')),  # <-- Add this line
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in login/logout/etc
]
