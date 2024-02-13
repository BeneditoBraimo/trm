from django.shortcuts import render, redirect
from .models import Location, Event

def successPage(request):
    title = "success"
    return render(request, 'successPage.html', {'title': title})


def index(request):
    title = 'TRM'
    return render(request, "index.html", {'title':title})


def addLocation(request):
    title = 'Location form'

    if request.method == 'POST':
        locationName = request.POST.get('name')
        locationDescription = request.POST.get('description')

        location = Location(
            name = locationName,
            description=locationDescription
        )

        location.save()
        return redirect(successPage)
    return render(request, 'locationForm.html', {'title': title})
    
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
        return redirect(successPage)

    locations = Location.objects.all()
    return render(request, "addEventForm.html", {'title': title, 'locations': locations})

def reportIncidend(request):
    title = "Incident form"

    return render(request, 'reportIncidentForm.html', {'title': title})