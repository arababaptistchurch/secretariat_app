# import datetime
# from datetime import datetime
# from app.models import Members
# from dateutil.relativedelta import relativedelta
# from django.db.models import Q


# class CustomFilters:

#     def __init__(self):
#         self.members = Members.objects.all()
#         members_not_children = self.members.filter(
#             date_of_birth__lt=datetime.now() - relativedelta(years=12)).all()
#         youth = self.members.filter(
#             date_of_birth__gte=datetime.now() - relativedelta(years=45), date_of_birth__lte=datetime.now() - relativedelta(years=18))
#         teens = self.members.filter(
#             date_of_birth__gte=datetime.now() - relativedelta(years=13), date_of_birth__lt=datetime.now() - relativedelta(years=18))
#         Single = self.members.filter(
#             date_of_birth__gte=datetime.now() - relativedelta(years=18), marital_status='single')
#         Married = self.members.filter(marital_status='married')
#         Widows_Widowers = self.members.filter(marital_status='widowed')
#         today_birthday_celebrants = self.members.filter(
#             date_of_birth__month=datetime.today().month, date_of_birth__day=datetime.today().day)
#         this_months_celebrants = self.members.filter(
#             date_of_birth__month=datetime.today().month)
#         WMU = self.members.filter(Q(marital_status='widowed') | Q(
#             marital_status='married'), gender='female')
#         MMU = self.members.filter(Q(marital_status='widowed') | Q(
#             marital_status='married'), gender='male')

#         self.filters = {
#             'All members': [i for i in self.members],
#             'All Members minus children': [i for i in members_not_children],
#             'Youths': [i for i in youth],
#             'Teens': [i for i in teens],
#             'Single': [i for i in Single],
#             'Married': [i for i in Married],
#             'Widows and Widowers': [i for i in Widows_Widowers],
#             "Today's Birthday Celebrants": [i for i in today_birthday_celebrants],
#             "This Month's Birthday Celebrants": [i for i in this_months_celebrants],
#             "WMU": [i for i in WMU],
#             "MMU": [i for i in MMU],
#             "Custom Numbers": ""
#         }

#     def number_generated(self, keyword):

#         return self.filters[keyword]
