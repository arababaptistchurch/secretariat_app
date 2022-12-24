from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testing', views.testing, name='testing'),
    path('new_member', views.new_member, name='new_member'),
    path('<int:member_id>/update_member', views.update_member, name='update_member'),
    path('datapage', views.data_page, name='datapage'),
]