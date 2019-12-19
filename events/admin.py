from django.contrib import admin
from .models import Article, Article2, SpeakerImg, SponsorImg

# Register your models here.
admin.site.register(Article)
admin.site.register(Article2)
admin.site.register(SpeakerImg)
admin.site.register(SponsorImg)