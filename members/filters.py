import django_filters
from app.models import Members


class MemberFilter(django_filters.FilterSet):

    society = django_filters.AllValuesFilter(lookup_expr='exact')
    gender = django_filters.AllValuesFilter(lookup_expr='exact')

    class Meta:
        model = Members
        fields = ['society', 'gender']
        # fields = {
        #     "society": ['exact'],
        #     "gender": ['exact'],
        #     "date_of_birth": ['exact']
        # }
