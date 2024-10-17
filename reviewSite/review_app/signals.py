from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Reviewer

@receiver(post_save, sender=User)
def create_reviewer(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        Reviewer.objects.create(user=instance, name=f"Reviewer {instance.username}")

@receiver(post_save, sender=User)
def save_reviewer(sender, instance, **kwargs):
    if hasattr(instance, 'reviewer'):
        instance.reviewer.save()