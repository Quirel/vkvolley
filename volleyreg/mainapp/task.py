from datetime import datetime as dt
import time

from volleyreg.celery import app as celery
from celery.utils.log import get_task_logger
from celery import group
# from celery.schedules import crontab

from mainapp.models import Player, RegisterTask
from vkapi_wrapper.models import Keys
from vkapi_wrapper.wrapper import VkWrapper


logger = get_task_logger(__name__)


@celery.task
def register_player(player_pk, key_title):
    """
    Create registration task for player
    IMPORTANT: task runs only, when 'manage.py process tasks' executed
    TODO: remove task if already exists for this player
    TODO: shared task decorator doesn't work
    """

    player = Player.objects.get(pk=player_pk)
    current_time = dt.today().time()
    if not player.registered:
        key = Keys.objects.get(title=key_title)
        vk = VkWrapper(key)
        vk.get_message()
        vk.comment_message('Testing. Name: {}, time: {}'.format(player.name, current_time))
        logger.info('Player: {}, registered, {}'.format(player, current_time))
        player.toggle_registered()
    else:
        logger.info('Player: {} already registered, {}'.format(player, current_time))


@celery.task
def register_task_dispatcher(key_title):
    """
    TODO: if no players need register -> pass
    :param key_title:
    :return:
    """
    players = Player.objects.all()
    key = Keys.objects.get(title=key_title)
    vk = VkWrapper(key)
    stop = False
    while not stop:
        vk.get_wall()
        msg = vk.get_message()
        if 'Запись на' in msg['text'] and 'Время игры' in msg['text'] and dt.today().date() == msg['date']:
            logger.info('Message found')
            task_list = [register_player.s(p.pk, key_title) for p in players]
            group(task_list).delay()
            stop = True
            logger.info('Tasks dispatched')
        else:
            time.sleep(5)
            logger.info('No message found')


# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Executes every Monday morning at 7:30 a.m.
#     activation = RegisterTask.objects.all().last().activation_time
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         register_task_dispatcher.s(''),
#     )
