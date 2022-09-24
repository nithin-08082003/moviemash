from django.contrib import admin
from django.urls import path
#import section
from . import views
from Posts.models import AllPosts
#create urls here

urlpatterns = [
    path('detail/<int:pk>/', views.Detail, name='detail'),
    path('photos-gallery/<str:photo_cat>/', views.PhotosDetail, name='photos-detail'),
]
