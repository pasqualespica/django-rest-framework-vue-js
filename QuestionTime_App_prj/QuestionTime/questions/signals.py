from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string

from questions.models import Question


@receiver(pre_save, sender=Question)
def addSlug_2_question(sender, instance, *arsgs, **kwargs):
    print("Dajeeeee")
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string

