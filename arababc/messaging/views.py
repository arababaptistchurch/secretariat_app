from django.shortcuts import render
from app.helpers import *
from .helper import *

# Create your views here.


def send_sms(request):

    sms = Sms()
    filters = CustomFilters()
    filters.filters['Custom Numbers'] = ''
    return render(request, 'messaging/messaging.html', {"group_list": filters.filters, "sms_balance": sms.balance_getter(), "sms_report": sms.report_getter()})
