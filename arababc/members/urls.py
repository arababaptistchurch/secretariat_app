from members.views import MembersListView, new_member
from django.urls import path
from . import views

urlpatterns = [
    path('new_member', views.new_member, name='new_member'),
    path('member_page/<slug:slug>', views.member_page, name='member_page'),
    path('datapage', MembersListView.as_view(), name='datapage'),
]
