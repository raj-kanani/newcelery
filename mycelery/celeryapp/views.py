from django.http import HttpResponse
from django.shortcuts import render
from .helper import user_mail
from .tasks import test_func, send_email_task, user_mail
from django.core.mail import send_mail


# testing for browser URL
def test(request):
    test_func.delay()
    return HttpResponse('mail testing success in browser URL. ')


# auto send mail with generate time schedule
def auto_send(request):
    send_email_task.delay()  # tasks.py method call
    return HttpResponse('Done mail success')


# send mail login user
def mail_all(request):
    user_mail.delay()
    return HttpResponse('sent success')
