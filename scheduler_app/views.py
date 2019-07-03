from django.shortcuts import render

def home(request):
	return render(request,'scheduler_app/home.html')