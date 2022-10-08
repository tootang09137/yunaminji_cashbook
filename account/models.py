from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    age = models.IntegerField(null= True, blank= True)
    address = models.CharField(max_length=50, null= True, blank= True)
    profile_image = models.ImageField(upload_to='images/', blank=True)