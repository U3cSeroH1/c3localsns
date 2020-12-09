from django.http import HttpResponse
from allauth.account.adapter import DefaultAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.models import SocialToken

import logging
logger = logging.getLogger("development")

class MyAccountAdapter(DefaultAccountAdapter):
    def __init__(self, request=None):
        super().__init__(request)

    def get_login_redirect_url(self, request):
        # リダイレクトするurl
        return 'http://127.0.0.1:8080'
    
    def pre_social_login(self, request, sociallogin):
        socialToken = SocialToken.objects.filter(sociallogin.account)
        logger.info(socialToken.token)
        raise ImmediateHttpResponse(HttpResponse("Closed for the day"))
