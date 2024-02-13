from django.db import models

class Agent(models.Model):
    firstName = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=False)
    code = models.CharField(max_length=11, blank=False, unique=True)

    def __str__(self):
        return (self.firstName, self.lastName)
    

class Recommendation(models.Model):
    description = models.CharField(max_length=500, blank=False)
    relevance = models.CharField(max_length=20)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT, blank=False)

    def __str__(self):
        return (self.description, self.relevance)
    
class Location(models.Model):
    name = models.CharField(max_length=60, blank=False)
    description = models.CharField(max_length=100)

    def __str__(self):
        return (self.name)


"""
    define OccurrenceType class model
    which has 'one-to-many' relationship with Occurrence class model
""" 
class IncidentType(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return (self.name)

class Occurrence(models.Model):
    occurrenceType = models.CharField(max_length=100, blank=False)
    occurrenceDate = models.DateField(blank=False)
    occurrenceDescription = models.CharField(max_length=200, blank=False)
    occurrenceStatus = models.CharField(max_length=15, blank=False)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=False)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)

    def __str__(self):
        return(self.occurrenceType, self.occurrenceDescription, self.occurrenceStatus)

class Event(models.Model):
    startingDate = models.DateField(blank=False)
    eventTitle = models.CharField(max_length=150, blank=False)
    eventDescription = models.CharField(max_length=250, blank=False)
    eventLocation = models.ManyToManyField(Location)

    def __str__(self):
        return(self.eventTitle, self.startingDate)