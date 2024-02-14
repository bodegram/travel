from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ACCOUNT_TYPE = (
        ('admin', 'admin'),
        ('superadmin', 'superadmin')
    )
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    
class Records(models.Model):
    record_id = models.CharField(max_length=100, null=True, unique=True)
    passenger_name = models.CharField(max_length=100, null=True)
    sponsor_name = models.CharField(max_length=100, null=True)
    reservation_taken_by = models.CharField(max_length=100, null=True)
    date_req = models.CharField(max_length=100, null=True)
    agent = models.CharField(max_length=100, null=True)
    penalties = models.CharField(max_length=100, null=True)
    deadline = models.CharField(max_length=100, null=True)
    fare_basis = models.CharField(max_length=100, null=True)
    booking_class = models.CharField(max_length=100, null=True)
    pnf_ref = models.CharField(max_length=100, null=True)
    baggage_allowance = models.CharField(max_length=100, null=True)
    validity = models.CharField(max_length=100, null=True)
    meal_preference = models.CharField(max_length=100, null=True)
    exchange_value = models.CharField(max_length=100, null=True)
    flier_no = models.CharField(max_length=100, null=True)
    nuc = models.CharField(max_length=100, null=True)
    taxes = models.CharField(max_length=100, null=True)
    lead = models.CharField(max_length=100, null=True)
    disc = models.CharField(max_length=100, null=True)
    total = models.CharField(max_length=100, null=True)
    nuc_one = models.CharField(max_length=100, null=True)
    nuc_two = models.CharField(max_length=100, null=True)
    taxes_one = models.CharField(max_length=100, null=True)
    taxes_two = models.CharField(max_length=100, null=True)
    total_one = models.CharField(max_length=100, null=True)
    total_two = models.CharField(max_length=100, null=True)
    lead_one = models.CharField(max_length=100, null=True)
    lead_two = models.CharField(max_length=100, null=True)
    disc_one = models.CharField(max_length=100, null=True)
    disc_two = models.CharField(max_length=100, null=True)
    gtotal_one = models.CharField(max_length=100, null=True)
    gtotal_two = models.CharField(max_length=100, null=True)
    
    
    
class Booking(models.Model):
    record = models.ForeignKey(Records, on_delete=models.CASCADE)
    arrival = models.CharField(max_length=100, null=True)
    departure = models.CharField(max_length=100, null=True)
    carrier = models.CharField(max_length=100, null=True)
    cl = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=100, null=True)
    departure_time = models.CharField(max_length=100, null=True)
    arrival_time = models.CharField(max_length=100, null=True)
    





    
   
    
    

