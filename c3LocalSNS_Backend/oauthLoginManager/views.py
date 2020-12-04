from django.shortcuts import render
import requests

from rest_framework import generics

from .serializers import DiscordExDataSerializer
from django.contrib.auth.models import User
# Create your views here.
from customDiscordProvider.views import DiscordOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)
from allauth.socialaccount.models import (
    SocialAccount,
)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class DiscordLogin(SocialLoginView):
    adapter_class = DiscordOAuth2Adapter


class DiscordExDataListAPIView(generics.RetrieveAPIView):
    """投稿モデルの取得（一覧）APIクラス"""
    #permission_classes = (IsAuthorOrReadOnly,)

    queryset = SocialAccount.objects.all()
    serializer_class = DiscordExDataSerializer


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        
        
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


# class UserNameAPI(APIView):
#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (permissions.IsAdminUser,)

#     def get(self, request, format=None):
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)

#     def post(self, request):
#         # 普通こんなことはしないが..
#         users = [User(username=name) for name in request.POST.getlist('name')]
#         User.objects.bulk_create(users)
#         return Response({'succeeded': True})

# def discordextradata(request):
#     data=SocialAccount.objects.get.extra_data
#     #follows=data.get('counts')
#     return render(request,'Path.to.html',{"data":data})

