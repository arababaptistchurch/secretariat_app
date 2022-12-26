from django.shortcuts import render, get_object_or_404
from app.models import *
from django.http import Http404

# Create your views here.


def new_member(request):
    state_list = ['as']
    files = Members.objects.all()
    return render(request, 'members/new_member.html', {'state_list': state_list, 'society_list': "osun", "files": files})


def member_page(request, member_id):
    member = get_object_or_404(Members, pk=member_id)
    return render(request, 'members/profile_page.html', {'member': member, 'profile_pic': member.profile_picture})


def data_page(request):

    members = Members.objects.all()
    return render(request, 'members/datapage.html', {'members': members})
