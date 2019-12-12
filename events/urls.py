from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('contacts/', views.contacts, name='contacts'),
    path('article/', views.article, name='article'),
    path('test/', views.test, name='test'),
	path('<slug>/', views.article_detail, name='article_detail'),
]
