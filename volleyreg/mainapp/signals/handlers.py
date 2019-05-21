from django.dispatch import receiver
from django.db.models.signals import post_save

from mainapp.models import Player
from mainapp.task import task_for_test


@receiver(post_save, sender=Player)
def register_player_after_save(sender, update_fields, instance, **kwargs):
    # TODO: specify timers
    print('signal recieved')
    print(instance)
    print(type(instance.pk), instance.pk)
    print(instance.date)
    print(instance.registered)
    if instance.date and not instance.registered:
        task_for_test.delay(player_pk=instance.pk)
    print('signal finished')
