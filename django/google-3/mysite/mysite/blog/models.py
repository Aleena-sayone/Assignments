from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk':self.pk })

    def total_likes(self):
        return self.likes.count()
