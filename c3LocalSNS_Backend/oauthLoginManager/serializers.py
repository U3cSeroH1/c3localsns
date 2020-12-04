from rest_framework import serializers
from allauth.socialaccount.models import (
    SocialAccount,
)



class DiscordExDataSerializer(serializers.ModelSerializer):
    """投稿シリアライザ"""
    class Meta:
        model = SocialAccount
        fields = '__all__'