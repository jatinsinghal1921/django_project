from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def createProfileObj(sender, instance, created, **kwargs):
    if created:
        profile_obj = Profile.objects.create(user=instance)
        profile_obj.save()
