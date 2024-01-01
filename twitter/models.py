from django.db import models
from django.conf import settings

# Create your models here.

class Twitt(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    # like = models.BooleanField()
    # def like_count(self):
    #     Twitt.objects.get()
    
    def __str__(self):
        return f'{self.owner}: {self.text}  | Created at {self.created_time} | Updated at {self.updated_time}'
