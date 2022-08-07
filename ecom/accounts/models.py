from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OnetoOneField(User, related_name='profile')
    short_description = models.CharField(max_length=1000)
    about = models.TextField()
    connected_profiles = models.ManyToManyField('Self', symmetrical=True)