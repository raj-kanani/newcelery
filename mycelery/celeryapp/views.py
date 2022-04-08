from django.http import HttpResponse
from django.shortcuts import render
from .helper import user_mail
from .tasks import test_func, send_email_task, user_mail
from django.core.mail import send_mail


def test(request):
    # user_mail()
    send_email_task.delay()  # tasks.py method call
    return HttpResponse('Done mail success')


# send mail login user
def mail_all(request):
    user_mail.delay()
    return HttpResponse('sent success')
