from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import *
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
