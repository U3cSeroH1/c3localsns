from django.contrib import admin
from .models import Post, Favorite

# Register your models here.
admin.site.register(Post)
admin.site.register(Favorite)