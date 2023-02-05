from django.shortcuts import render
from app.helpers import *
from .helper import *
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required

# Create your views here.


sms = Sms()
filters = CustomFilters()


@login_required(login_url='/users/login')
def get_filter(request):

    if request.method == 'POST':

        message = request.POST['message']
        numbers = request.POST['numbers']

        sms.sms_sender('Araba Bc', numbers, message)

    # return render(request, 'messaging/messaging.html', {"group_list": filters.filters, "sms_balance": sms.balance_getter(), "sms_report": sms.report_getter()})
    return render(request, 'messaging/messaging.html', {"group_list": filters.filters})


@login_required(login_url='/users/login')
def send_sms(request):

    print(os.environ['DBNAME'])

    selected_group = request.GET.get('filter')

    numbers = filters.filters[selected_group]
    resp = [{'name': f'{i.first_name} {i.surname}',
             'phone_number': i.phone_number} for i in numbers]

    return JsonResponse(resp, safe=False)
