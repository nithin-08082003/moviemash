from django.contrib import admin
from django.urls import path
#import section
from . import views
#create urls here

urlpatterns = [
    path('', views.Home, name='home'),
    path('search/', views.Search, name='search'),
    path('feedback/', views.FeedbackView, name='feedback'),
    path('about/', views.AboutView, name='about'),
]
