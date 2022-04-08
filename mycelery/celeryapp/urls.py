from . import views
from django.urls import path


urlpatterns = [
    path('test', views.test, name='test'),
    path('', views.mail_all, name='mail')
]
