from datetime import datetime as dt

from volleyreg.celery import app as celery

from mainapp.models import Player
from vkapi_wrapper.models import Keys
from vkapi_wrapper.wrapper import VkWrapper


@celery.task
def task_for_test(player_pk, key_title='Testing'):
    """
    Create registration task for player
    IMPORTANT: task runs only, when 'manage.py process tasks' executed
    TODO: remove task if already exists for this player
    TODO: shared task decorator doesn't work
    """
    player = Player.objects.get(pk=player_pk)
    current_time = dt.today().time()
    key = Keys.objects.get(title=key_title)
    vk = VkWrapper(key)
    vk.get_message()
    vk.comment_message('Testing. Name: {}, time: {}'.format(player.name, current_time))
