import requests
import os
from dotenv import load_dotenv
import pandas as pd
import datetime
from datetime import datetime
from app.models import Members
from dateutil.relativedelta import relativedelta
from django.db.models import Q


class Sms():

    def __init__(self):
        self.url_for_get = f'https://portal.nigeriabulksms.com/api/?username={os.environ.get("sms_username")}&password={os.environ.get("sms_password")}&action'
        self.url_for_post = f'https://portal.nigeriabulksms.com/api/?username={os.environ.get("sms_username")}&password={os.environ.get("sms_password")}'

    def balance_getter(self):
        url = f'{self.url_for_get}=balance'
        balance = int(requests.get(url=url).json()['balance'])
        return balance

    def report_getter(self):
        url = f'{self.url_for_get}=reports'
        balance = requests.get(url=url).json()
        return balance

    def sms_sender(self, sender, phone_numbers, message):
        msg_number = f'{self.url_for_post}&message={message}&sender={sender}&mobiles={phone_numbers}'
        send_sms = requests.post(msg_number)
        return send_sms


def age_group(new):
    this_year = datetime.today().year
    age = this_year - new.year
    if age <= 12:
        return 'Children'
    elif 12 < age <= 17:
        return 'Teen'
    elif 17 < age <= 45:
        return 'Youth'
    elif 45 < age <= 70:
        return 'Adult'
    else:
        return "Elder"


class NumberGenerate:

    def __init__(self):

        # self.group_list = {'All Members':, 'All Members minus children', 'Youths', 'Teens', 'Single', 'Married', 'Widows and Widowers',
        #                    "Today's Birthday Celebrants", "This Month's Birthday Celebrants", 'WMU', 'MMU',
        #                    "Custom Number(s)"}
        members = Members.objects.all()
        members_not_children = members.filter(
            date_of_birth__lt=datetime.now() - relativedelta(years=12)).all()
        youth = members.filter(
            date_of_birth__gte=datetime.now() - relativedelta(years=45), date_of_birth__lte=datetime.now() - relativedelta(years=18))
        teens = members.filter(
            date_of_birth__gte=datetime.now() - relativedelta(years=13), date_of_birth__lt=datetime.now() - relativedelta(years=18))
        Single = members.filter(
            date_of_birth__gte=datetime.now() - relativedelta(years=18), marital_status='single')
        Married = members.filter(marital_status='married')
        Widows_Widowers = members.filter(marital_status='widowed')
        today_birthday_celebrants = members.filter(
            date_of_birth__month=datetime.today().month, date_of_birth__day=datetime.today().day)
        this_months_celebrants = members.filter(
            date_of_birth__month=datetime.today().month)
        WMU = members.filter(Q(marital_status='widowed') | Q(
            marital_status='married'), gender='female')
        MMU = members.filter(Q(marital_status='widowed') | Q(
            marital_status='married'), gender='male')

        self.filters = {
            'All members': [i.phone_number for i in members],
            'All Members minus children': [i.phone_number for i in members_not_children],
            'Youths': [i.phone_number for i in youth],
            'Teens': [i.phone_number for i in teens],
            'Single': [i.phone_number for i in Single],
            'Married': [i.phone_number for i in Married],
            'Widows and Widowers': [i.phone_number for i in Widows_Widowers],
            "Today's Birthday Celebrants": [i.phone_number for i in today_birthday_celebrants],
            "This Month's Birthday Celebrants": [i.phone_number for i in this_months_celebrants],
            "WMU": [i.phone_number for i in WMU],
            "MMU": [i.phone_number for i in MMU]
        }

    def number_generated(self, keyword):

        return self.filters[keyword]
