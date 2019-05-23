from django.apps import AppConfig


class MainappConfig(AppConfig):
    name = 'mainapp'
    verbose_name = 'Запись игроков'

    def ready(self):
        import mainapp.signals.handlers
