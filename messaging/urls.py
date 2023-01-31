from django.urls import path

from . import views

urlpatterns = [
    path('send-text', views.get_filter, name='send_sms'),
    path('get-filters', views.send_sms, name='get_filter'),

]
