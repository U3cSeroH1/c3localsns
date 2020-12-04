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

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.db.models import Q

class DiscordLogin(SocialLoginView):
    adapter_class = DiscordOAuth2Adapter


class DiscordExDataListAPIView(generics.ListAPIView):
    """投稿モデルの取得（一覧）APIクラス"""
    #permission_classes = (IsAuthorOrReadOnly,)
    
    serializer_class = DiscordExDataSerializer
    queryset = SocialAccount.objects.all()

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('id',)


    def get_queryset(self, *args, **kwargs):
        queryset_list = SocialAccount.objects.all()
        query_f = self.request.GET.get("f") #ForeignKeyのフィルタリングは、get_querysetのオーバーライドで対応
        if query_f:
            queryset_list = queryset_list.filter(
                    Q(user__id__icontains=query_f)
                    ).distinct()
        return queryset_list

#user idをpostしたらそのuser idをもつsocialaccountのextra_dataが帰ってくるapi
#socialaccountのpkはidで，user id ≠ socialaccountのpkのid
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        
        
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


class UserNameAPI(APIView):
    #authentication_classes = (authentication.TokenAuthentication,)
    #permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

    def post(self, request):
        # 普通こんなことはしないが..
        users = [User(username=name) for name in request.POST.getlist('name')]
        User.objects.bulk_create(users)
        return Response({'succeeded': True})

# def discordextradata(request):
#     data=SocialAccount.objects.get.extra_data
#     #follows=data.get('counts')
#     return render(request,'Path.to.html',{"data":data})

