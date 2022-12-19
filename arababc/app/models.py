from django.db import models

# Create your models here.

class Members(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    second_phone_number = models.CharField(max_length=200)
    residential_address  = models.CharField(max_length=200)
    neighborhood  = models.CharField(max_length=200)
    lga  = models.CharField(max_length=200)
    residential_state   = models.CharField(max_length=200)
    lat_lng   = models.CharField(max_length=200)
    state_of_origin  = models.CharField(max_length=200)
    state_lga   = models.CharField(max_length=200)
    date_of_birth  = models.DateField(max_length=200)
    permanent_address   = models.CharField(max_length=200)
    occupation   = models.CharField(max_length=200)
    marital_status =  models.CharField(max_length=200)
    wedding_date =  models.CharField(max_length=200)
    baptism =  models.CharField(max_length=200)
    society =  models.CharField(max_length=200)
    
    
class Positions(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True, editable=True)
    department = models.CharField(max_length=200)
    start_date =  models.DateField(max_length=200)
    end_date =  models.DateField(max_length=200)



class Abc_Families(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    family_name =models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200) #to be deleted
    email = models.EmailField(null=True) #to be deleted
    residential_address =  models.CharField(max_length=200) #to be deleted
    google_suggested_address =  models.CharField(max_length=200) #to be deleted
    Neigborhood =  models.CharField(max_length=200) #to be deleted
    lga =  models.CharField(max_length=200) #to be deleted
    state = models.CharField(max_length=200) #to be deleted
    coordinates = models.CharField(max_length=200) #to be deleted