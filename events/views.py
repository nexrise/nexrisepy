from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.

articles = Article.objects.all().order_by('-date')

def index(request):
	return render(request, 'events/home.html', {'articles':articles})

def about(request):
	return render(request, 'events/about-us.html', {'articles':articles})

def events(request):
	return render(request, 'events/events.html', {'articles':articles})

def contacts(request):
	return render(request, 'events/contacts.html', {'articles':articles})

def article(request):
	return render(request, 'events/article.html', {'articles':articles})

def test(request):
	return render(request, 'events/test.html', {'articles':articles})

def article_detail(request, slug):
	# return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	return render(request, 'events/detail.html', {'article':article, 'articles':articles})