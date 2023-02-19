from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
def home(request):
    context = {}
    contact_list = Country.objects.all()
    paginator = Paginator(contact_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['countries'] = page_obj

  
    return render(request, 'index.html', context)

def about(request, id):
    context={}
    context['country'] = Country.objects.get(id=id)
   
    return render(request, 'about.html', context)

def deal(request):
    context = {}
    context['countries'] = Country.objects.all()
    context['princes'] = Price_Range.objects.all()
    context['deals'] = CityTown.objects.all()
#pagination
    contact_list = CityTown.objects.all()
    paginator = Paginator(contact_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['countries'] = page_obj
    ##

    if request.method == "GET":
        get = request.GET
        country = get.get('country',False)
        price = get.get('price',False)
        if country and price:
            pr = Price_Range.objects.filter(id=price).first()
            country = Country.objects.filter(id=country).first()
            deals = country.cities_towns.all()
            deals = deals.filter(prince__lte=pr.startprice).all()
            deals = deals.filter(prince__gte=pr.endprice).all()
            context['deals'] = deals
            

    return render(request, 'deals.html', context)


def reservation(request, id):
    context = {}
    context['numberofguests'] = NumberofGuest.objects.all()
    citytown = CityTown.objects.get(id=id)
    context['citytown'] = citytown
    if request.method == "POST":
        post = request.POST
        name = post.get('name',False)
        phone = post.get('phone',False)
        numberofguest = post.get('numberofguest',False)
        data = post.get('data',False)
        if name and phone and numberofguest and data:
            rever = Reservation.objects.create(name=name,phone=phone,data=data,numberofguest_id=numberofguest,direction=citytown)
            rever.save()
   
    return render(request, 'reservation.html', context)



    

     








