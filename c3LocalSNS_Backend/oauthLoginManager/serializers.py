from rest_framework import serializers
from allauth.socialaccount.models import (
    SocialAccount,
)



class DiscordExDataSerializer(serializers.ModelSerializer):
    """投稿シリアライザ"""
    class Meta:
        model = SocialAccount
        fields = '__all__'


class IdPostTest(serializers.Serializer):
    """投稿シリアライザ"""

    id = serializers.CharField()
