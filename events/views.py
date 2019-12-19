from django.shortcuts import render
from django.http import HttpResponse
from .models import Article2, SpeakerImg, SponsorImg


# Create your views here.


def index(request):
	article_list = Article2.objects.all().order_by('-date')
	return render(request, 'events/home.html', {'article_list':article_list})

def about(request):
	article_list = Article2.objects.all().order_by('-date')
	return render(request, 'events/about-us.html', {'article_list':article_list})

def events(request):
	article_list = Article2.objects.all().order_by('-date')
	return render(request, 'events/events.html', {'article_list':article_list})

def contacts(request):
	article_list = Article2.objects.all().order_by('-date')
	return render(request, 'events/contacts.html', {'article_list':article_list})

def article_detail(request, slug):
	# return HttpResponse(slug)
	article_list = Article2.objects.all().order_by('-date') #This is for nav bar Important
	article_link = Article2.objects.get(slug=slug)
	speakers = SpeakerImg.objects.all().filter(slug__slug=slug)
	sponsors = SponsorImg.objects.all().filter(slug__slug=slug)
	return render(request, 'events/detail.html', {
	'article_list':article_list,
	'article_link':article_link,
	'speakers':speakers,
	'sponsors':sponsors,
	})



