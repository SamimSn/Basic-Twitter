from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.

class Twitt(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='twitt_id')
    
    def __str__(self):
        return f'{self.owner}: {self.text}  | Created at {self.created_time} | Updated at {self.updated_time}'
    
    def number_of_likes(self):
        return self.likes.count()