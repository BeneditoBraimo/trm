from django.shortcuts import render
from .forms import AgentForm, RecommendationForm, OccurrenceForm, EventForm, LocationForm

def index(request):
    title = 'Home'
    return render(request, "index.html", {'title':title})

def addEvent(request):
    title = 'Event form'
    if request.method == 'POST':
        event = EventForm(request.POST)
        if event.is_valid():
            event.save()
            return render(request,'index.html', {'title': title})
        else:
            event = EventForm()
    return render(request, "addEventForm.html", {'title': title})