from .models import Member
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save,sender = Member)
def notification(sender, instance , created,**kwargs):
    if created:
        print("---------Some action has been occur in table---------")