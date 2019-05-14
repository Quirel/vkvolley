from django.db import models


class Player(models.Model):
    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    name = models.CharField(verbose_name='Имя', max_length=128, unique=True)
    register_4 = models.BooleanField(verbose_name='Четверг', default=False)
    register_6 = models.BooleanField(verbose_name='Суббота', default=False)

    def __str__(self):
        return self.name

