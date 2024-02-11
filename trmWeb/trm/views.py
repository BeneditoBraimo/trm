from django.shortcuts import render, redirect
from .models import Location, Event

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
        locationId = location.id

        event = Event(
            startingDate = startingDate,
            eventTitle = eventTitle,
            eventDescription = eventDescription,
            eventLocation = locationId
        )
        event.save()
        # add code to load 'success' template
        objName = "event"
        return redirect('sucessPage.html')

    locations = Location.objects.all()
    return render(request, "addEventForm.html", {'title': title, 'locations': locations})