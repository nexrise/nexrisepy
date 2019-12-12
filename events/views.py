from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.



def index(request):
	return render(request, 'events/home.html')

def about(request):
	return render(request, 'events/about-us.html')

def events(request):
	return render(request, 'events/events.html')

def contacts(request):
	return render(request, 'events/contacts.html')

def article(request):
	return render(request, 'events/article.html')

def test(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'events/test.html', {'articles':articles})

def article_detail(request, slug):
	# return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	return render(request, 'events/detail.html', {'article':article})