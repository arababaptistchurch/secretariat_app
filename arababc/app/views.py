from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Members, AbcFamilies, JointEvents
import datetime as dt
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from collections import Counter
import json

# Create your views here.


def index(request):
    time_threshold = datetime.now() - relativedelta(years=18)
    all_members = Members.objects.all()
    members_not_children = Members.objects.filter(
        date_of_birth__lt=time_threshold).all()
    societies = [i.society for i in members_not_children]
    new = zip(Counter(societies).keys(), Counter(societies).values())
    chart_data = dict(new)
    family = AbcFamilies.objects.all()
    Family_name = [i.family_name for i in family]
    latitiude = [float(i.coordinates.split(',')[0][1:]) for i in family]
    longitude = [float(i.coordinates.split(',')[1][:-1].strip(' '))
                 for i in family]
    items = [list(x) for x in zip(Family_name, latitiude, longitude)]
    event = JointEvents.objects.filter(date__lt=datetime.today())
    event_list = [{'Title': i.title, 'Description': i.description,
                   'Date': i.date, 'due_date': i.date - dt.date.today()
                   } for i in event if i.event_completed is None]

    return render(request, 'index.html', {'all_members': all_members[:5], 'count': len(members_not_children),
                                          "members_count": Members.objects.all().count(), "chart_data": chart_data,
                                          'family_coordinates': items, "upcoming": event.count(), "event_list": event_list})


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
