from members.views import *
from django.urls import path
from . import views

urlpatterns = [
    path('new_member', views.new_member, name='new_member'),
    path('member_page/<int:id>', views.member_page, name='member_page'),
    path('datapage', views.data_page, name='datapage'),
]
