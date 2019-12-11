from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	return render(request, 'events/home.html')

def about(request):
	return render(request, 'events/about-us.html')

def events(request):
	return render(request, 'events/events.html')

def contacts(request):
	return render(request, 'events/contacts.html')