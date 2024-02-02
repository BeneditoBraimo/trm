from django.db import models

class Agent(models.Model):
    firstName = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=False)
    code = models.CharField(max_length=11, blank=False, unique=True)

    def __str__(self):
        return str(self.firstName, self.lastName)
