from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    title = 'Home'
    return render(request, "index.html", {'title':title})

# Create your views here.
