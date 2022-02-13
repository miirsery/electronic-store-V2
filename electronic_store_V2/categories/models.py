from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    URL_category = models.URLField(max_length=200)
    image = models.ImageField(upload_to=None , height_field=None , width_field=None , max_length=100)