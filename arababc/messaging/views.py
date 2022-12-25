from django.shortcuts import render
from .helper import *

# Create your views here.


def send_sms(request):

    sms = Sms()
    num = NumberGenerate()
    sms_report = sms.report_getter()
    # report = sms.report_getter(phone_counter)
    # number_of_pending = report['status'].count("Submitted")
    # number_of_delivered = report['status'].count('DELIVERED')

    return render(request, 'messaging/messaging.html', {"group_list": num.group_list, "sms_balance": sms.balance_getter(), "sms_report": sms_report})
