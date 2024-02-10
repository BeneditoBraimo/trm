from django.shortcuts import render
from .models import Location

def index(request):
    title = 'Home'
    return render(request, "index.html", {'title':title})

def addEvent(request):
    title = 'Event form'
    if request.method == 'POST':
        startingDate = request.POST.get('startingDate')
        eventTitle = request.POST.get('eventTitle')
        eventDescription = request.POST.get('eventDescription')

        eventLocation = request.POST.get('eventLocation')

        location = Location.objects.get(name=eventLocation)
        locationId = Location.id
    return render(request, "addEventForm.html", {'title': title})