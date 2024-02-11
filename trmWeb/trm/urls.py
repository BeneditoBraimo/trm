from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addEvent/", views.addEvent, name="addEvent"),
    path("addLocation/", views.addLocation, name="addLocation"),
]