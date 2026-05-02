from django.db import models
from django.contrib.auth.models import AbstractUser

from authentication.manager import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()