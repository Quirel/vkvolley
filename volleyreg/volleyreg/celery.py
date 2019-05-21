import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volleyreg.settings')

app = Celery('volleyreg')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'register all players': {
        'task': 'mainapp.task.register_task_dispatcher',
        'schedule': crontab(hour='5', minute='26', day_of_week='wed,fri'),
    },
}

