from rest_framework import serializers
from django.contrib.auth.models import User # 追加

class UserSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = User()
        fields = '__all__'