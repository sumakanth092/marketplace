from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # example extension
    is_seller = models.BooleanField(default=False)
