from django.shortcuts import render

# Create your views here.
from Posts.models import AllPosts , PhotoCategory , GalleryImg

def PhotosDetail(request,photo_cat):
    detail_photo_post = GalleryImg.objects.filter(photo_category__category_title = photo_cat).order_by('?')
    img_gallery_count = detail_photo_post.count()
    random_photos = PhotoCategory.objects.all().order_by('?')[:11]
    context = {
        'detail_photo_post':detail_photo_post,
        'random_photos':random_photos,
        'photo_cat':photo_cat,
        'img_gallery_count':img_gallery_count,
    }
    return render(request,'Detail/photos_detail.html',context)

def Detail(request,pk):
    detail_post = AllPosts.objects.get(id=pk)
    next_random_posts = AllPosts.objects.all().order_by('?')[:5]
    recent_photos = PhotoCategory.objects.all()[:10]
    recent_posts = AllPosts.objects.all()[:10]
    context = {
        'detail_post':detail_post,
        'recent_photos':recent_photos,
        'recent_posts':recent_posts,
        'next_random_posts':next_random_posts,
    }
    return render(request,'Detail/detail.html',context)
