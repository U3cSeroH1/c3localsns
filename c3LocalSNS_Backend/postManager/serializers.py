from rest_framework import serializers
from .models import Post, Favorite
from userManager.serializers import UserSerializer
from django.contrib.auth.models import User


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
    
    def create(self, validated_data):
        user = validated_data['user']
        post = validated_data['post']
        if Favorite.objects.filter(user=user, post=post).count() > 0:
            raise serializers.ValidationError(detail="Duplicated Favorite")
        return Favorite.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    """投稿シリアライザ"""
    class PostFavoriteSerializer(FavoriteSerializer):
        class Meta:
            model = Favorite
            exclude = ['post']
            depth = 1

    favorites = PostFavoriteSerializer(read_only=True, many=True)

    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        depth = 1
    
    def create(self, validated_data):
        validated_data['author'] = validated_data.get('author_id', None)
        if validated_data['author'] is None:
            raise serializers.ValidationError("author not found.")
        del validated_data['author_id']

        return Post.objects.create(**validated_data)