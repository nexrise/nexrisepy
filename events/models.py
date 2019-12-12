from django.db import models

# Create your models here.

class Article(models.Model):
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)
	img = models.ImageField(upload_to='img/')
	title = models.CharField(max_length=100)
	title2 = models.CharField(max_length=100)
	title3 = models.CharField(max_length=100)
	event_date = models.DateTimeField(auto_now_add=True)
	event_hotel = models.CharField(max_length=100, default='edit')
	event_country = models.CharField(max_length=100, default='edit')
	heading1 = models.CharField(max_length=100)
	body1 = models.TextField()
	heading2 = models.CharField(max_length=100)
	body2 = models.TextField()
	heading3 = models.CharField(max_length=100)
	body3 = models.TextField()
	
	def __str__(self):
		return self.title