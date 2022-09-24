from django.contrib import admin

# Register your models here.

from . models import AllPosts , Category
from . models import PhotoCategory, GalleryImg

class AllPostsAdmin(admin.ModelAdmin):
    list_display = ('category','headline','created')


class GalleryImgAdmin(admin.ModelAdmin):
    list_display = ('photo_category', 'gallery_images')

#for all posts
admin.site.register(AllPosts,AllPostsAdmin)
admin.site.register(Category)

#for photos
admin.site.register(PhotoCategory)
admin.site.register(GalleryImg, GalleryImgAdmin)