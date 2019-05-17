from django.db import models


class Keys(models.Model):
    class Meta:
        verbose_name = 'Ключи'
        verbose_name_plural = 'Ключи'

    title = models.CharField(verbose_name='Title', max_length=128, blank=True)
    app_id = models.CharField(verbose_name='App ID', max_length=64,)
    access_token = models.CharField(verbose_name='Access key', max_length=256)
    group_id = models.CharField(verbose_name='Group id', max_length=64)

    def __str__(self):
        return 'keys for app id: {}'.format(self.app_id)
