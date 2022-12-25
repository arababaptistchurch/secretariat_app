from django.urls import path

from . import views

urlpatterns = [
    path('send-text', views.send_sms, name='send_sms')
]
