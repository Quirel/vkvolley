from django.db import models

from datetime import datetime as dt
from background_task import background
from unidecode import unidecode

from vkapi_wrapper.wrapper import VkWrapper
from vkapi_wrapper.models import Keys


class Player(models.Model):
    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    name = models.CharField(verbose_name='Имя', max_length=128, unique=True)
    registered = models.BooleanField(verbose_name='ОК', default=False)
    date = models.DateField(verbose_name="Дата", null=True)

    def __str__(self):
        return self.name

    def toggle_registered(self):
        if self.registered:
            self.registered = False
        else:
            self.registered = True
        self.save()

    @staticmethod
    @background()
    def task_for_test(name, key_title='Testing'):
        """
        Create registration task for player
        IMPORTANT: task runs only, when 'manage.py process tasks' executed
        TODO: remove task if already exists for this player
        """

        current_time = dt.today().time()
        key = Keys.objects.get(title=key_title)
        vk = VkWrapper(key)
        vk.get_message()
        vk.comment_message('Testing. Name: {}, time: {}'.format(name, current_time))

    def save(self, *args, **kwargs):
        """
        Check if player need to register and not registered yet
        Start task date = player.date - 1 day
        Start = datetime.time(hours=9, minutes=55)
        Stop task time = start + 30 minutes
        TODO: specify timers
        """
        if self.date and not self.registered:
            self.task_for_test(creator=self, name=unidecode(self.name), verbose_name='Register {}'.format(self.name))

        super().save(*args, **kwargs)




