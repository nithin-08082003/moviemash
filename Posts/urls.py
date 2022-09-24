from django.contrib import admin
from django.urls import path
#import section
from . import views
from . models import AllPosts
#create urls here

urlpatterns = [
    path('boxoffice/',views.Boxoffice ,name="boxoffice"),
    path('hollywood/',views.Hollywood ,name="hollywood"),
    path('style/',views.Style ,name="style"),
    path('news/',views.News ,name="news"),
    path('gossips/',views.Gossips ,name="gossips"),
    path('upcomings/',views.Upcomings ,name="upcomings"),
    path('photos/',views.Photos ,name="photos"),
    path('webstories/',views.Webstories ,name="webstories"),
]