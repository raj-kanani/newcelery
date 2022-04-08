from __future__ import absolute_import, unicode_literals
import os
from celery.schedules import crontab
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycelery.settings')
app = Celery('mycelery')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
# app.config_from_object('django.conf:settings')
app.config_from_object(settings, namespace='CELERY')

# celery beat setting send mail every day for all users
app.conf.beat_schedule = {
    'send-mail-every-day-at-5': {
        'task': 'celeryapp.tasks.send_email_task',
        'schedule': crontab(hour=6, minute=10),
        # 'args' :(2,)
    }
}

# celery beat settings
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
