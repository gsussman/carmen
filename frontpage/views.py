from django.shortcuts import render
from signup.forms import LocationInput, TripShare
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import HttpResponse
from signup.models import Location, Trip
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore

# Create your views here.

import json


def search(request):
    form = LocationInput()
    if request.method == "POST":
        form = LocationInput(request.POST)
        if form.is_valid():
            t = Trip(trip_name = form.cleaned_data['city'])
            t.save()
            if Location.objects.filter(google_id=form.cleaned_data['google_id']).exists():
                l = Location.objects.get(google_id=form.cleaned_data['google_id'])
                l.trips.add(t)
                l.save()
            else:
                form.save()
                l = Location.objects.get(google_id=form.cleaned_data['google_id'])
                l.trips.add(t)
                l.save()
            if request.user.is_authenticated():
                t.owner = request.user
                t.save()
                return HttpResponseRedirect('/trips/')
            else:
                request.session['trip-id'] = t.id
                return HttpResponseRedirect('/auth/') 
    return render(request, 'frontpage/search.html', {'form': form})

def trips(request):
    trips = Trip.objects.filter(owner = request.user)
    tripshared = Trip.objects.filter(shared_with = request.user)
    if 'trip-id' in request.session:
        tid = request.session['trip-id']
        trip = Trip.objects.get(id = tid)
        trip.owner = request.user
        trip.save()
        trips = Trip.objects.filter(owner = request.user)
    return render(request, 'frontpage/trips.html', 
        {'trips' : trips,
         'tripshared' : tripshared})

def trip_details(request, name='unknown'):
    name = name.replace('-', ' ').title()
    trip = Trip.objects.get(trip_name = name, owner = request.user)
    locations = trip.location_set.all()
    formloc = LocationInput()
    formtripshare = TripShare(instance=trip, prefix = 'triptag')
    if request.method == "POST":
        if 'triptag' in request.POST:
            tripshare = TripShare(request.POST, instance=trip, prefix = 'triptag')
            if tripshare.is_valid():
                tripshare.save()
        else:
            form = LocationInput(request.POST)
            if form.is_valid():
              t = trip
              if Location.objects.filter(google_id=form.cleaned_data['google_id']).exists():
                  l = Location.objects.get(google_id=form.cleaned_data['google_id'])
                  l.trips.add(t)
                  l.save()
              else:
                  form.save()
                  l = Location.objects.get(google_id=form.cleaned_data['google_id'])
                  l.trips.add(t)
                  l.save() 
    return render(request, 'frontpage/trip_details.html', 
        {'trip' : trip,
        'locations': locations,
        'form' : formloc,
        'tripform' : formtripshare})

def trip_details_shared(request, name='unknown'):
    name = name.replace('-', ' ').title()
    trip = Trip.objects.get(trip_name = name, shared_with = request.user)
    locations = trip.location_set.all()
    formloc = LocationInput()
    formtripshare = TripShare(instance=trip, prefix = 'triptag')
    if request.method == "POST":
        if 'triptag' in request.POST:
            tripshare = TripShare(request.POST, instance=trip, prefix = 'triptag')
            if tripshare.is_valid():
                tripshare.save()
        else:
            form = LocationInput(request.POST)
            if form.is_valid():
              t = trip
              if Location.objects.filter(google_id=form.cleaned_data['google_id']).exists():
                  l = Location.objects.get(google_id=form.cleaned_data['google_id'])
                  l.trips.add(t)
                  l.save()
              else:
                  form.save()
                  l = Location.objects.get(google_id=form.cleaned_data['google_id'])
                  l.trips.add(t)
                  l.save() 
    return render(request, 'frontpage/trip_details.html', 
        {'trip' : trip,
        'locations': locations,
        'form' : formloc,
        'tripform' : formtripshare})

class RegView(RegistrationView):
    def get_success_url(self, user):
        return '/trips/'

        # pulled from http://stackoverflow.com/questions/20108706/passing-success-url-to-cbv-django-registration

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/trips/'

def auth(request):
    return render(request, 'frontpage/auth.html', {})
