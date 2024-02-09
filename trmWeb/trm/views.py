from django.shortcuts import render


def index(request):
    title = 'Home'
    return render(request, "index.html", {'title':title})

def addEvent(request):
    title = 'Event form'
    
    return render(request, "addEventForm.html", {'title': title})