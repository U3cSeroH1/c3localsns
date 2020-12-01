from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text    

