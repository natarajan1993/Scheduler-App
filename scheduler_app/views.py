from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def home(request):
	events = Event.objects.all()
	events_list = list(events)
	print(events)
	return render(request,'scheduler_app/home.html')

def about(request):
	return render(request,'scheduler_app/about.html')

def scheduler(request):
	return render(request,'scheduler_app/Scheduler.html')