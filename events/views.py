from django.shortcuts import render
from app.models import JointEvents
import datetime
from django.contrib.auth.decorators import login_required
# from
# Create your views here.


@login_required(login_url='/users/login')
def calendar(request):

    event = JointEvents.objects.filter(date__lt=datetime.date.today())
    parent_list = [{'title': i.title, 'description': i.description,
                   'date': i.date, 'due_date': i.date - datetime.date.today()
                    } for i in event if i.event_completed is None]

    event_color = 'RGB'
    return render(request, 'events/calendar.html', {"event": event, "event_color": event_color, "parent_list": parent_list})
