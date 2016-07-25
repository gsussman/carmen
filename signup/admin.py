from django.contrib import admin


# Register your models here.
from .models import Location, Trip

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)

class TripAdmin(admin.ModelAdmin):
	list_display = ('trip_name', 'owner', 'id')
admin.site.register(Trip, TripAdmin)