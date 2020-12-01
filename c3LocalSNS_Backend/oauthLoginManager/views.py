from django.shortcuts import render
import requests

# Create your views here.
from customDiscordProvider.views import DiscordOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView




class DiscordLogin(SocialLoginView):
    adapter_class = DiscordOAuth2Adapter

