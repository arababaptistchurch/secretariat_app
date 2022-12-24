from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Members

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def testing(request):
    return HttpResponse("Hello, world.")


def new_member(request):
    state_list = ['as']
    files = Members.objects.all()
    return render(request, 'members/index.html', {'state_list': state_list, 'society_list': "osun", "files": files})


def update_member(request, member_id):
    files = get_object_or_404(Members, pk=member_id)
    return render(request, 'members/index.html', {'state_list': state_list, 'society_list': "osun", "files": files})


def data_page(request):

    members = Members.objects.all()
    return render(request, 'members/datapage.html', {'members': members})

# def profile_page(request):
