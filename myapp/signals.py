from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, DarkModePreference

@receiver(post_save, sender=CustomUser)
def create_dark_mode_preference(sender, instance, created, **kwargs):
    if created:
        DarkModePreference.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_dark_mode_preference(sender, instance, **kwargs):
    instance.darkmodepreference.save()
