from django.conf.urls import url, include
from . import views
import allauth

# Create a new class that redirects the user to the index page, if successful at logging
#class MyRegistrationView(RegistrationView):
#    def get_success_url(self,request, user):
#        return '/rango/'

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^search/$', views.search, name='search'),
    url(r'^trips/$', views.trips, name='trips'),
    url(r'^trips/(?P<name>[-\w]+)/$', views.trip_details, name ='trip_details'),
    url(r'^trips/shared/(?P<name>[-\w]+)/$', views.trip_details_shared, name ='trip_details'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^accounts/', include('allauth.urls')),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
]