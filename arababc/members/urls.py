from . import views
from django.urls import path

urlpatterns = [
    path('new_member', views.new_member, name='new_member'),
    path('member_page/<int:member_id>', views.member_page, name='member_page'),
    path('datapage', views.data_page, name='datapage'),
]
