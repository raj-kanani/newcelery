from time import sleep
from celery import shared_task
# add mail
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from mycelery import settings


@shared_task(bind=True)
def test_func(self):
    # operations
    for i in range(10):
        print(i)
    return 'Done'


@shared_task
def send_email_task():
    sleep(5)
    # parameter : (body , message body
    send_mail('CELERY SEND IN MAIL SUCCESS',
              'CELLARY PASSED',
              'raj.kanani@plutustec.com',  # sender
              ['bhaktiraiyani18@gmail.com'],  # receiver
              fail_silently=False
              )
    return None


#  login user send mail .

@shared_task(bind=True)
def user_mail(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = 'this is celery testing'
        message = 'celery message success in your mail id.'
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message = message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True
        )
        return "success mail passed"
