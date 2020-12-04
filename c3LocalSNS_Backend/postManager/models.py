from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    authorname = models.CharField(max_length=50, default='',)
    authoravatar = models.CharField(max_length=100, default='',)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

