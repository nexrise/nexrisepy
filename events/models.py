from django.db import models

# Create your models here.

class Article(models.Model):
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)
	img = models.ImageField(upload_to='img/', default='http://via.placeholder.com/200')
	title = models.CharField(max_length=100)
	title2 = models.CharField(max_length=100)
	title3 = models.CharField(max_length=100)
	event_date = models.DateTimeField(auto_now_add=True)
	event_hotel = models.CharField(max_length=100, default='edit')
	event_country = models.CharField(max_length=100, default='edit')
	
	heading1 = models.CharField(max_length=100, null=True, blank=True)
	body1 = models.TextField(null=True, blank=True)
	heading2 = models.CharField(max_length=100, null=True, blank=True)
	body2 = models.TextField(null=True, blank=True)
	heading3 = models.CharField(max_length=100, null=True, blank=True)
	body3 = models.TextField(null=True, blank=True)
	heading4 = models.CharField(max_length=100, null=True, blank=True)
	body4 = models.TextField(null=True, blank=True)
	
	name1 = models.CharField(max_length=50, default='speaker name')
	speaker1 = models.ImageField(upload_to='img/', default='http://via.placeholder.com/200')
	name2 = models.CharField(max_length=50, default='speaker name')
	speaker2 = models.ImageField(upload_to='img/', default='http://via.placeholder.com/200')
	name3 = models.CharField(max_length=50, default='speaker name')
	speaker3 = models.ImageField(upload_to='img/', default='http://via.placeholder.com/200')
	name4 = models.CharField(max_length=50, default='speaker name')
	speaker4 = models.ImageField(upload_to='img/', default='http://via.placeholder.com/200')
	name5 = models.CharField(max_length=50, default='speaker name')
	speaker5 = models.ImageField(upload_to='img/', default='http://via.placeholder.com/200')
	name6 = models.CharField(max_length=50, default='speaker name')
	speaker6 = models.ImageField(upload_to='img/', default='http://via.placeholder.com/200')
	
	def __str__(self):
		return self.title