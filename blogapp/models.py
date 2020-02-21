from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="")
    body = RichTextUploadingField()

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=True, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.TextField(max_length=20)
    comment_thumbnail_url = models.TextField(max_length=300)
    comment_textfield = models.TextField()

class BlogData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    def __str__(self):
        return self.title