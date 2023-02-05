from django.urls import path
from . import views


urlpatterns = [
    path('login', views.logs_user, name='login'),
    path('logout_user', views.logout_user, name='logout')
]
