from django.shortcuts import render
from .forms import AgentForm, RecommendationForm, OccurrenceForm, EventForm, LocationForm

def index(request):
    title = 'Home'
    return render(request, "index.html", {'title':title})

# Create your views here.
