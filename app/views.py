from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Create your views here.
def  login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Invalid credentials')
            
    return render(request, 'login.html')




def dashboard(request):
    return render(request, 'Dashboard.html')

def newRecord(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        passenger_name = request.POST.get('passenger_name')
        sponsor_name = request.POST.get('sponsor_name')
        reservation_taken_by = request.POST.get('reservation_taken_by')
        date_req = request.POST.get('date_req')
        agent = request.POST.get('agent')
        deadline = request.POST.get('deadline')
        penalties = request.POST.get('penalties')
        fare_basis = request.POST.get('fare_basis')
        booking_class = request.POST.get('booking_class')
        pnf_ref = request.POST.get('pnf_ref')
        baggage_allowance = request.POST.get('baggage_allowance')
        validity = request.POST.get('validity')
        meal_preference = request.POST.get('meal_preference')
        exchange_value = request.POST.get('exchange_value')
        flier_no = request.POST.get('flier_no')
        nuc = request.POST.get('nuc')
        taxes = request.POST.get('taxes')
        lead = request.POST.get('lead')
        disc = request.POST.get('disc')
        total = request.POST.get('total')
        nuc_one = request.POST.get('nuc_one')
        nuc_two = request.POST.get('nuc_two')
        taxes_one = request.POST.get('taxes_one')
        taxes_two = request.POST.get('taxes_two')
        total_one = request.POST.get('total_one')
        total_two = request.POST.get('total_two')
        lead_one = request.POST.get('lead_one')
        lead_two = request.POST.get('lead_two')
        disc_one = request.POST.get('disco_one')
        disc_two = request.POST.get('disco_two')
        gtotal_one = request.POST.get('gtotal_one')
        gtotal_two = request.POST.get('gtotal_two')
        arrival = request.POST.get('arrival')
        departure = request.POST.get('departure')
        carrier = request.POST.get('carrier')
        cl = request.POST.get('cl')
        date = request.POST.get('date')
        departure_time = request.POST.get('departure_time')
        arrival_time = request.POST.get('arrival_time')
        user_record = Records(
            record_id=record_id,
            passenger_name=passenger_name,
            sponsor_name=sponsor_name,
            reservation_taken_by=reservation_taken_by,
            date_req=date_req,
            agent=agent,
            deadline=deadline,
            penalties=penalties,
            fare_basis=fare_basis,
            booking_class=booking_class,
            pnf_ref=pnf_ref,
            baggage_allowance=baggage_allowance,
            validity=validity,
            meal_preference=meal_preference,
            exchange_value=exchange_value,
            flier_no=flier_no,
            nuc=nuc,
            taxes=taxes,
            lead=lead,
            disc=disc,
            total=total,
            nuc_one=nuc_one,
            nuc_two=nuc_two,
            taxes_one=taxes_one,
            taxes_two=taxes_two,
            total_one=total_one,
            total_two=total_two,
            lead_one=lead_one,
            lead_two=lead_two,
            disc_one=disc_one,
            disc_two=disc_two,
            gtotal_one=gtotal_one,
            gtotal_two=gtotal_two,
             
        )
        user_record.save()
        
        booking = Booking
        
        
    return render(request, 'record.html')


def signout(request):
    logout(request)
    return redirect('login')



def retrieveRecord(request):
    return render(request, 'retrieve-record.html')