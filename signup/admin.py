from django.contrib import admin


# Register your models here.
from .models import Location, Trip, LocImage

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)

class TripAdmin(admin.ModelAdmin):
	list_display = ('trip_name', 'owner', 'id')
admin.site.register(Trip, TripAdmin)

class LocImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(LocImage, LocImageAdmin)