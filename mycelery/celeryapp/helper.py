from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from django.core.mail import send_mail


# send mail using without celery
def user_mail():
    send_mail('CELERY WORK', 'CELERY DONE',
              'raj.kanani@plutustec.com',  # sender
              ['raj.kanani1487@gmail.com'],  # receiver
              fail_silently=False
              )
    print('mail sent successsss..')
    return None
