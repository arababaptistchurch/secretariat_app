from django.urls import path

from . import views

urlpatterns = [
    path('send-text', views.send_sms, name='send_sms'),
    path('get-filters', views.get_filter, name='get_filter'),

]
