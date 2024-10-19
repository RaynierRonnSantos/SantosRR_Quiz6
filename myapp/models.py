from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, unique=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class DarkModePreference(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_dark_mode = models.BooleanField(default=False)  # False by default (light mode)

    def __str__(self):
        return f"{self.user.username}'s Dark Mode Preference"

