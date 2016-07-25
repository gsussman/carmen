from django import forms

from .models import Location, Trip


class LocationInput(forms.ModelForm):

    class Meta:
        model = Location
        widgets = {
            'name' : forms.TextInput(attrs = {'placeholder': 'I want to go to...', 'size': '15', 'type': 'hidden'}),
            'google_id' : forms.TextInput(attrs = {'type': 'hidden'}),  
            'address' : forms.TextInput(attrs = {'type': 'hidden'}),
            'city' : forms.TextInput(attrs = {'type': 'hidden'}),
            'lat' : forms.TextInput(attrs = {'type': 'hidden'}),
            'lng' : forms.TextInput(attrs = {'type': 'hidden'}),   
            'trips' : forms.TextInput(attrs = {'type': 'hidden'}),  
            'image_url' : forms.TextInput(attrs = {'type': 'hidden'}), 

        }
        fields = ('name', 'google_id', 'address', 'city', 'lat', 'lng', 'trips', 'image_url')

class TripShare(forms.ModelForm):

    class Meta:
        model = Trip
        fields = ('shared_with', 'trip_name')
        