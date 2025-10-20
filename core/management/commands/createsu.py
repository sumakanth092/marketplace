from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Create a superuser if none exists'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        if not User.objects.filter(username=username).exists():
            print('Creating superuser...')
            User.objects.create_superuser(username=username, password=password, email=email)
        else:
            print('Superuser already exists')
