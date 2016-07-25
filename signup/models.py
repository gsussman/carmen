from __future__ import unicode_literals

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Trip(models.Model):
 owner = models.ForeignKey(User, null=True, related_name = 'trips')
 shared_with = models.ManyToManyField(User, blank = True, related_name = 'shared')
 trip_name = models.CharField(max_length=25, null=True)
 start_date = models.DateField(null=True, blank=True)
 end_date = models.DateField(null=True, blank=True)

 def __unicode__(self):
  return self.trip_name

 def url_readable_state(self):
	return self.trip_name.replace(' ', '-')

class Location(models.Model):
 name = models.CharField(max_length=250)
 google_id = models.CharField(max_length=250)
 address = models.CharField(max_length=250)
 city = models.CharField(max_length=250)
 lat = models.FloatField()
 lng = models.FloatField()
 trips = models.ManyToManyField(Trip, blank=True)
 image_url = models.URLField(null=True, blank=True)

 def __unicode__(self):
  return self.name