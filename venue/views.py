from django.shortcuts import render
import urllib.request
from .models import  Venue
from django.db.models import Q
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen('https://www.python.org')


# Create your views here.
#gmaps.configure(api_key='AIzaSyDLJ0y_piefTd33M6ySRtEgztYSdmjDzLc')


#新版

def venuesearch(request):
    venues = Venue.objects.all()
    return render(request, 'venuesearch.html',locals())
#

def venueresult(request):
    venues = Venue.objects.all()
    query1 = request.POST.get("city")
    query2 = request.POST.get("type")

    if query1:
        venues = venues.filter(
            Q(locationName__icontains=query2) &
            Q(location__icontains=query1)).distinct()
    elif query2:
        venues = venues.filter(
            Q(locationName__icontains=query2) &
            Q(location__icontains=query1)).distinct()

    return render(request, 'venueresult.html', locals())










