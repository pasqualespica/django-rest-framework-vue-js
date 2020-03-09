from django.contrib.auth.models import User
from django.db.models.signals import post_save # User mandera' il seganle post_save ogni volta che viene salvata
from django.dispatch import receiver # decoratore per ricevere uesto seganale
from profiles.models import Profile # crere un nuovo profile


# Per poterla utlizzare va fatta una configurazione in 
# __init__.py
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("singal.s.py => Created ...", created)
    if created:
        Profile.objects.create(user=instance)

