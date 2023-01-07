from django.shortcuts import render, get_object_or_404
from app.models import *
from django.http import Http404
from .data import *

# Create your views here.


def new_member(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')

    return render(request, 'members/new_member.html', {'state_list': state_list, 'society_list': society})


def member_page(request, slug):
    member = get_object_or_404(Members, slug=slug)
    return render(request, 'members/profile_page.html', {'member': member})


def data_page(request):

    members = Members.objects.all()
    return render(request, 'members/datapage.html', {'members': members})
