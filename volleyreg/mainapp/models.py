from django.db import models

from vkapi_wrapper.models import Keys


class Player(models.Model):
    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    name = models.CharField(verbose_name='Имя', max_length=128, unique=True)
    registered = models.BooleanField(verbose_name='ОК', default=False)

    def __str__(self):
        return self.name

    def toggle_registered(self):
        if self.registered:
            self.registered = False
        else:
            self.registered = True
        self.save()


class RegisterTask(models.Model):
    class Meta:
        verbose_name = 'Register task'
        verbose_name_plural = 'Register_tasks'

    date_created = models.DateField(verbose_name='Created', auto_now_add=True, editable=False)
    activation_time = models.DateTimeField(verbose_name='Init time', null=True)
    players = models.CharField(verbose_name='Players', blank=True, editable=False, max_length=256)
