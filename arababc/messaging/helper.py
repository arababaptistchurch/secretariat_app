import requests
import os
from dotenv import load_dotenv
import pandas as pd
import datetime
from datetime import datetime


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


def month_day(new):
    current_month = new.month
    day = new.day
    month_and_day = (current_month, day)
    return month_and_day


def month(new):
    current_month = new.month

    return current_month


class NumberGenerate:

    def __init__(self):
        self.engine = 'postgresql://postgres:icui4cu4u@34.170.97.205:5432/arababc'
        self.df = pd.read_sql('select * from Members', con=self.engine)
        # self.df = pd.read_csv('/Users/akinbodebams/PycharmProjects/arabs/new.csv')
        self.drop_duplicate()
        self.df['age_group'] = self.df['date_of_birth'].apply(age_group)
        self.df['month_and_day'] = self.df['date_of_birth'].apply(month_day)
        self.df['month'] = self.df['date_of_birth'].apply(month)
        self.group_list = ['All Members', 'All Members minus children', 'Youths', 'Teens', 'Single', 'Married', 'Widows and Widowers',
                           "Today's Birthday Celebrants", "This Month's Birthday Celebrants", 'WMU', 'MMU',
                           "Custom Number(s)"]

    def number_getter(self, keyword):
        all_members = self.df['phone_number']
        all_members_wo_children = self.df[self.df.age_group !=
                                          'Children'].phone_number
        youths = self.df[self.df.age_group == 'Youth'].phone_number
        teens = self.df[self.df.age_group == 'Teen'].phone_number
        widowed = self.df[self.df.marital_status == 'widowed'].phone_number
        singles = self.df[self.df.marital_status == 'single'].phone_number
        married = self.df[self.df.marital_status == 'married'].phone_number
        b_day = self.df[
            self.df.month_and_day == (datetime.today().date().month, datetime.today().date().day)].phone_number
        month_b_day = self.df[self.df.month ==
                              datetime.today().month].phone_number
        wmu = self.df[(self.df.gender == 'female') & (
            self.df.marital_status == 'married')].phone_number
        mmu = self.df[(self.df.gender == 'male') & (
            self.df.marital_status == 'married')].phone_number

        if keyword.lower() == 'all members':
            return all_members
        elif keyword == 'All Members minus children':
            return all_members_wo_children
        elif keyword.lower() == 'youths':
            return youths
        elif keyword.lower() == 'teens':
            return teens
        elif keyword.lower() == 'married':
            return married
        elif keyword.lower() == 'widows and widowers':
            return widowed
        elif keyword.lower() == 'single':
            return singles
        elif keyword == "Today's Birthday Celebrants":
            return b_day
        elif keyword == "This Month's Birthday Celebrants":
            return month_b_day
        elif keyword.lower() == 'wmu':
            return wmu
        elif keyword.lower() == 'mmu':
            return mmu
        else:
            return ''

    def drop_duplicate(self):
        self.df.drop_duplicates(
            subset=['phone_number'], inplace=True, keep="first")
