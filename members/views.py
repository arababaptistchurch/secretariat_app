from django.shortcuts import render, get_object_or_404
from app.models import *
from django.http import Http404
from .data import *
from .filters import MemberFilter
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .helper import Families
from django.contrib.auth.decorators import login_required
import os

# Create your views here.


def new_member(request):
    if request.method == 'POST':

        new_member = Members(
            first_name=request.POST.get('first_name'),
            middle_name=request.POST.get('middle_name'),
            surname=request.POST.get('surname'),
            maiden_name=request.POST.get('maiden_name'),
            gender=request.POST.get('gender').lower(),
            phone_number=request.POST.get('phone_number'),
            second_phone_number=request.POST.get('second_phone_number'),
            email=request.POST.get('email'),
            residential_address=request.POST.get('residential_address'),
            neighborhood=request.POST.get('neighborhood'),
            lga=request.POST.get('lga'),
            residential_state=request.POST.get('state'),
            lat_lng=f"[{request.POST.get('lat')},{request.POST.get('lng')}]",
            state_of_origin=request.POST.get('state_of_origin'),
            state_lga=request.POST.get('state_lga'),
            date_of_birth=request.POST.get('date_of_birth'),
            permanent_address=request.POST.get('permanent_address'),
            occupation=request.POST.get('occupation'),
            marital_status=request.POST.get('marital_status'),
            wedding_date=request.POST.get('wedding_date'),
            baptism=request.POST.get('baptism'),
            society=request.POST.get('society'),
        )
        new_member.save()
        fams = Families()
        if fams.family_checker(marital_status=request.POST.get('marital_status').lower(), date_of_birth=request.POST.get('date_of_birth'), gender=request.POST.get('gender').lower()):
            title = fams.title_adder(request.POST.get('gender'), request.POST.get(
                'date_of_birth'), request.POST.get('marital_status').lower())
            AbcFamilies(family_name=f"{title} {request.POST.get('first_name')} {request.POST.get('surname')}",
                        phone_number=request.POST.get('phone_number'),
                        email=request.POST.get('email'),
                        residential_address=request.POST.get(
                            'residential_address'),
                        neigborhood=request.POST.get('neighborhood'),
                        lga=request.POST.get('lga'),
                        state=request.POST.get('state'),
                        coordinates=f"[{request.POST.get('lat')},{request.POST.get('lng')}]",
                        member=new_member).save()
        position_items = {
            "department": request.POST.getlist('department'),
            "position": request.POST.getlist('position'),
            "start_date": request.POST.getlist('start_date'),
            "end_date": request.POST.getlist('end_date'),
        }

        for i in range(0, len(position_items['department'])):

            Positions(position=position_items['position'][i],
                      department=position_items['department'][i],
                      start_date=position_items['start_date'][i],
                      end_date=position_items['end_date'][i],
                      member=new_member).save()

    return render(request, 'members/new_member.html', {'state_list': states,
                                                       'society_list': society,
                                                       "marital_status": marital_status,
                                                       "department": departments,
                                                       "google_apikey": os.getenv("google_apikey")})


@login_required(login_url='/users/login')
def member_page(request, id):
    member = get_object_or_404(Members, id=id)
    return render(request, 'members/profile_page.html', {'member': member})


@login_required(login_url='/users/login')
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
