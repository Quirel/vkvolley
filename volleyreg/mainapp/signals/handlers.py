from django.dispatch import receiver
from django.db.models.signals import post_save

from mainapp.models import Player, RegisterTask
from mainapp.task import register_player, register_task_dispatcher


# @receiver(post_save, sender=Player)
# def register_player_after_save(sender, update_fields, instance, **kwargs):
#     # TODO: specify timers
#     print('signal recieved')
#     print(instance)
#     print(type(instance.pk), instance.pk)
#     print(instance.date)
#     print(instance.registered)
#     if instance.date and not instance.registered:
#         task_for_test.delay(player_pk=instance.pk)
#     print('signal finished')


# @receiver(post_save, sender=RegisterTask)
# def register_player_after_save(sender, update_fields, instance, **kwargs):
#     """
#     schedule a task on specified date and time
#     """
#     if instance.activation_time:
#         if instance.activation_time:
#             register_task_dispatcher.delay()
#             # TODO: create task

