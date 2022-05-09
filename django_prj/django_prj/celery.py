import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_prj.settings')

app = Celery("django_prj")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Запуск task(foo_3) 1 раз в минуту
app.conf.beat_schedule = {
    'test-schedule-function': {
        'task': 'todo.tasks.foo_3',
        'schedule': crontab(),
        'args': (16, 6),
    },
}

