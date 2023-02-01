from django.shortcuts import render, get_object_or_404
from app.models import *
from django.http import Http404
from .data import *
from .filters import MemberFilter
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.


def new_member(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')

    return render(request, 'members/new_member.html', {'state_list': state_list, 'society_list': society})


def member_page(request, id):
    member = get_object_or_404(Members, id=id)
    return render(request, 'members/profile_page.html', {'member': member})


def data_page(request):
    members = Members.objects.all()

    if request.method == 'GET' and 'date_filter' in request.GET:

        if request.GET['date_filter'] == "Today's Birthday":
            members = Members.objects.filter(date_of_birth__month=datetime.today(
            ).month, date_of_birth__day=datetime.today().day)
        elif request.GET['date_filter'] == "This Month's Birthdays":
            members = Members.objects.filter(
                date_of_birth__month=datetime.today().month)
        elif request.GET['date_filter'] == "This Week's Birthdays":
            members = Members.objects.filter(date_of_birth__month=datetime.today().month,
                                             date_of_birth__day__range=[datetime.today().day, datetime.today().day + 7])

    member_filter = MemberFilter(request.GET, queryset=members)
    context = {
        "member_filter": member_filter
    }
    return render(request, 'members/datapage.html', context)
