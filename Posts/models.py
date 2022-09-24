from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.title


class AllPosts(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=False)
    image = models.ImageField(upload_to='all/', blank=False)
    image_credit = models.CharField(max_length=100, blank=True)
    headline = models.CharField(max_length=300, blank=False)
    summary = models.CharField(max_length=500, blank=True)
    description = RichTextField(blank=False, null=True)
    embed = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.headline

#photo model

class PhotoCategory(models.Model):
    category_title = models.CharField(max_length=50, blank=False)
    main_img = models.ImageField(upload_to='photos/', blank=False)
    category_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        ordering = ['-category_created']


class GalleryImg(models.Model):
    photo_category = models.ForeignKey(
        PhotoCategory, on_delete=models.CASCADE, null=True, blank=False)
    gallery_images = models.ImageField(upload_to='photos/', blank=False)
    img_uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-img_uploaded']
