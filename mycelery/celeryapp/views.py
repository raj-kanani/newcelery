from django.http import HttpResponse
from django.shortcuts import render
from .helper import user_mail
from .tasks import test_func, send_email_task, user_mail
from django.core.mail import send_mail
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


# testing for browser URL
def test(request):
    result = test_func.delay()
    print(result.backend)
    return HttpResponse('mail testing success in browser URL. ')


# auto send mail with generate time schedule
def auto_send(request):
    send_email_task.delay()  # tasks.py method call
    return HttpResponse('Done mail success')


# send mail login user
def mail_all(request):
    user_mail.delay()
    return HttpResponse('sent success')


# every login user schedule any task / custom task & periodic task
def send_mail_perticular_time(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=11, minute=53)
    task = PeriodicTask.objects.create(crontab=schedule, name='schedule_task' + '5',
                                       task='celeryapp.tasks.user_mail')  # name must be unique
    # args=json.dumps(([2, 3])) #args in pass the tuple in array value 2,3
    return HttpResponse('perticular task done')
