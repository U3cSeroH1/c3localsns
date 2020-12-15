from rest_framework import serializers
from django.contrib.auth.models import User # 追加
from allauth.socialaccount.models import SocialAccount
import json

class UserSerializer(serializers.ModelSerializer):
    extra_data = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ['password']
    
    def get_extra_data(self, obj):
        extra_data = SocialAccount.objects.filter(user=obj).first().extra_data
        return extra_data