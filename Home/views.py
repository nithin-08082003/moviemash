from django.shortcuts import render , redirect
from django.db.models import Q
from . forms import FeedbackForm
from django.contrib import messages

# Create your views here.
from Posts.models import AllPosts , PhotoCategory , GalleryImg

def Home(request):
    four_recent_posts = AllPosts.objects.all()[:4]
    home_random_photos = PhotoCategory.objects.all()[:15]
    recent_first_posts = AllPosts.objects.all()[4:10]
    home_upcomings = AllPosts.objects.filter(category__title='upcomings')[:8]
    random_pics = GalleryImg.objects.all().order_by('?')[:30]
    recent_second_posts = AllPosts.objects.all()[10:16]
    recent_last_posts = AllPosts.objects.all()[16:25]
    context = {
        'four_recent_posts':four_recent_posts,
        'home_random_photos':home_random_photos,
        'recent_first_posts':recent_first_posts,
        'home_upcomings':home_upcomings,
        'recent_second_posts':recent_second_posts,
        'random_pics':random_pics,
        'recent_last_posts':recent_last_posts ,
        }
    return render(request,'Home/home.html',context)


def Search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_allposts = AllPosts.objects.filter(
            Q(headline__icontains=searched) |
            Q(summary__icontains=searched) |
            Q(description__icontains=searched)
        )

        total_allposts = search_allposts.count()

        search_photo_posts = PhotoCategory.objects.filter(
            Q(category_title__icontains=searched)
        )
        total_photos_posts = search_photo_posts.count()
        
        return render(request,'Home/search.html',{
            'searched':searched , 
            'search_allposts':search_allposts,
            'search_photo_posts':search_photo_posts,
            'total_allposts':total_allposts,
            'total_photos_posts':total_photos_posts,
            })
    else:
        return render(request,'Home/search.html',{})

def FeedbackView(request):
    feedback = FeedbackForm()
    if request.method == 'POST':
        feedback = FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
            messages.success(request, 'thank you for providing  your valuable feedback!')
            return redirect('feedback')

    context = {'feedback':feedback}
    return render(request,'Home/feedback.html',context)


def AboutView(request):
    context={}
    return render(request,'Home/about.html',context)
