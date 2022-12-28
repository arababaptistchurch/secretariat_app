from django.shortcuts import render
from .helper import *

# Create your views here.


def send_sms(request):

    sms = Sms()
    num = NumberGenerate()
    return render(request, 'messaging/messaging.html', {"group_list": num.filters, "sms_balance": sms.balance_getter(), "sms_report": sms.report_getter()})
