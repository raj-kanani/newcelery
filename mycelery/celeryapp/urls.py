from . import views
from django.urls import path


urlpatterns = [
    path('test', views.test, name='test'),
    path('auto', views.auto_send, name='auto'),
    path('', views.mail_all, name='mail')
]
