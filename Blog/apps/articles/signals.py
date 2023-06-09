from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Articles
from django.utils.text import slugify

from apps.questions.models import Question

@receiver(pre_save,sender = Articles)
def add_slug(sender,instance,*args,**kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug



@receiver(pre_save,sender = Question)
def add_slug(sender,instance,*args,**kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        instance.slug = slug