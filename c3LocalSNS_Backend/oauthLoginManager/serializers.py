from rest_framework import serializers
import json
from allauth.socialaccount.models import (
    SocialAccount,
)



class DiscordExDataSerializer(serializers.ModelSerializer):
    extra_data = serializers.SerializerMethodField()

    class Meta:
        model = SocialAccount
        fields = ['extra_data']
        # fields = '__all__'

    def get_extra_data(self, obj):
        return obj.extra_data


class IdPostTest(serializers.Serializer):
    """投稿シリアライザ"""

    id = serializers.CharField()
