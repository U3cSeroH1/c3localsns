"""c3LocalSNS_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import HttpResponse

API_TITLE = 'c3の社内SNSアプリ'
API_DESCRIPTION = 'c3の社内SNSアプリです！！！黙れ！！！！！！！'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/postManager/', include('postManager.urls')),
    path('api/v1/userManager/', include('userManager.urls')),
    path('api/v1/oauthLoginManager/', include('oauthLoginManager.urls')),
    path('api/v1/oauthLoginManager/', include('customDiscordProvider.urls')),

    path('api-auth/', include('rest_framework.urls')),
    
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),


    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),

    path('accounts/', include('allauth.urls')),

    path('', lambda request: HttpResponse('インデックス'), name='index'),

]
