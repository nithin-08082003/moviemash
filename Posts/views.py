from django.shortcuts import render

# Create your views here.
from . models import AllPosts
from . models import PhotoCategory

def Photos(request):
    top_photos_post = PhotoCategory.objects.all()[:1]
    four_photos_post = PhotoCategory.objects.all()[1:5]
    remain_photos_post = PhotoCategory.objects.all()[5:]
    context = {
        'top_photos_post':top_photos_post,
        'four_photos_post':four_photos_post,
        'remain_photos_post':remain_photos_post,
    }
    return render(request,'Posts/photos.html',context)

def Webstories(request):
    return render(request, 'Posts/webstories.html')

def News(request):
    top_post = AllPosts.objects.filter(category__title='news')[:1]
    four_posts = AllPosts.objects.filter(category__title='news')[1:5]
    remain_posts = AllPosts.objects.filter(category__title='news')[5:]
    context = {
        'top_post':top_post,
        'four_posts':four_posts,
        'remain_posts':remain_posts,
    }
    return render(request,'Posts/news.html',context)

def Gossips(request):
    top_post = AllPosts.objects.filter(category__title='gossips')[:1]
    four_posts = AllPosts.objects.filter(category__title='gossips')[1:5]
    remain_posts = AllPosts.objects.filter(category__title='gossips')[5:]
    context = {
        'top_post':top_post,
        'four_posts':four_posts,
        'remain_posts':remain_posts,
    }
    return render(request,'Posts/gossips.html',context)

def Hollywood(request):
    top_post = AllPosts.objects.filter(category__title='hollywood')[:1]
    four_posts = AllPosts.objects.filter(category__title='hollywood')[1:5]
    remain_posts = AllPosts.objects.filter(category__title='hollywood')[5:]
    context = {
        'top_post':top_post,
        'four_posts':four_posts,
        'remain_posts':remain_posts,
    }
    return render(request,'Posts/hollywood.html',context)

def Boxoffice(request):
    top_post = AllPosts.objects.filter(category__title='boxoffice')[:1]
    four_posts = AllPosts.objects.filter(category__title='boxoffice')[1:5]
    remain_posts = AllPosts.objects.filter(category__title='boxoffice')[5:]
    context = {
        'top_post':top_post,
        'four_posts':four_posts,
        'remain_posts':remain_posts,
    }
    return render(request,'Posts/boxoffice.html',context)

def Upcomings(request):
    top_post = AllPosts.objects.filter(category__title='upcomings')[:1]
    four_posts = AllPosts.objects.filter(category__title='upcomings')[1:5]
    remain_posts = AllPosts.objects.filter(category__title='upcomings')[5:]
    context = {
        'top_post':top_post,
        'four_posts':four_posts,
        'remain_posts':remain_posts,
    }
    return render(request,'Posts/upcomings.html',context)

def Style(request):
    top_post = AllPosts.objects.filter(category__title='style')[:1]
    four_posts = AllPosts.objects.filter(category__title='style')[1:5]
    remain_posts = AllPosts.objects.filter(category__title='style')[5:]
    context = {
        'top_post':top_post,
        'four_posts':four_posts,
        'remain_posts':remain_posts,
    }
    return render(request,'Posts/style.html',context)
