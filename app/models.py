from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

	