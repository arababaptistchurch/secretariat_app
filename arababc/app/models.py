from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Members(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    maiden_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    second_phone_number = models.CharField(
        max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    residential_address = models.CharField(
        max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    lga = models.CharField(max_length=100, blank=True, null=True)
    residential_state = models.CharField(max_length=100, blank=True, null=True)
    lat_lng = models.CharField(max_length=100, blank=True, null=True)
    state_of_origin = models.CharField(max_length=100, blank=True, null=True)
    state_lga = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    permanent_address = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=100, blank=True, null=True)
    wedding_date = models.CharField(max_length=100, blank=True, null=True)
    baptism = models.CharField(max_length=100, blank=True, null=True)
    society = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, null=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.middle_name} {self.surname}'

    def get_absolute_url(self):
        return reverse("member_page", kwargs={"slug": self.slug})

    class Meta:
        managed = True
        db_table = 'members'
        verbose_name_plural = 'members'


class Positions(models.Model):
    # id = models.IntegerField(primary_key=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.CharField(max_length=100, blank=True, null=True)
    end_date = models.CharField(max_length=100, blank=True, null=True)
    member = models.ForeignKey(
        Members, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'positions'
        verbose_name_plural = 'positions'


class AbcFamilies(models.Model):
    id = models.IntegerField(primary_key=True)
    family_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    residential_address = models.CharField(
        max_length=100, blank=True, null=True)
    google_suggested_address = models.CharField(
        max_length=100, blank=True, null=True)
    # Field name made lowercase.
    neigborhood = models.CharField(
        db_column='Neigborhood', max_length=100, blank=True, null=True)
    lga = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    coordinates = models.CharField(max_length=100, blank=True, null=True)
    member = models.ForeignKey(
        'Members', models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return self.family_name

    class Meta:
        managed = True
        db_table = 'abc_families'
        verbose_name_plural = 'abc_families'


class Calendar(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'calendar'


class JointEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    # Field name made lowercase.
    title = models.CharField(
        db_column='Title', max_length=120, blank=True, null=True)
    # Field name made lowercase.
    description = models.CharField(
        db_column='Description', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    event_completed = models.DateField(blank=True, null=True)
    calendar = models.ForeignKey(
        Calendar, models.DO_NOTHING, blank=True, null=True)
    visitation = models.ForeignKey(
        'Visitations', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'joint_events'


class Visitations(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    day_visited = models.CharField(max_length=100, blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True, null=True)
    scheduled_visitation = models.DateField(blank=True, null=True)
    summary = models.CharField(max_length=500, blank=True, null=True)
    family = models.ForeignKey(
        AbcFamilies, models.DO_NOTHING, blank=True, null=True)
    visitation_status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'visitations'
