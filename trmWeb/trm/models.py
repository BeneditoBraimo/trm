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
