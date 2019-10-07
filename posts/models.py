from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=30)
    content = RichTextField()
    image = models.ImageField(blank=True,)
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post_list')


class Comment(models.Model):
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    text = RichTextField()
    created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('posts:post_list')

    def __str__(self):
        return self.text