from django.db import models

from django.db import models

class SiteSetting(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=200)

