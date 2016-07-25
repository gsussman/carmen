from django.contrib import admin


# Register your models here.
from .models import Location, Trip

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)

class TripAdmin(admin.ModelAdmin):
	pass
admin.site.register(Trip, TripAdmin)