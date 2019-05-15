from django.db import models


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

