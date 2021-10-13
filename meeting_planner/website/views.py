from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("Hello, I'm raghad, 23 years old, I'm working hard to change the world! Watch me.")
