from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """投稿シリアライザ"""
    class Meta:
        model = Post
        fields = '__all__'