from django import forms
from .models import Agent, Recommendation, Event, Occurrence, Location

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

class RecommendationForm(forms.ModelForm):
    class Meta:
        model= Recommendation
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class OccurrenceForm(forms.ModelForm):
    class Meta:
        model = Occurrence
        fields = '__all__'

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'