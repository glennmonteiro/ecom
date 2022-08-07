from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    link = models.URLField()
    creator = models.ForeignKey(User, related_name='comments')
    likers = models.ManyToManyField(User, related_name='liked_posts')



class Comment(models.Models):
    body = models.CharField(max_length=500)
    creator = models.ForeignKey(User, related_name='comments')
    likers = models.ManyToManyField(User, related_name='liked_comments')
    post = models.ForeignKey(Post, related_name='comments')
    parent = models.ForeignKey('Self', related_name='children', null=True)



