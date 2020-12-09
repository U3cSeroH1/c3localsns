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
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, FavoriteViewSet
from . import views


#router = SimpleRouter()
#router.register('', PostViewSet)

#urlpatterns = router.urls

urlpatterns = [
    path('posts', PostViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'update': 'update'
    })),
    path('posts/list/', views.PostListAPIView.as_view()),
    path('posts/create/', views.PostCreateAPIView.as_view()),
    path('posts/detail/<int:pk>/', views.PostDetailAPIView.as_view()),
    path('favorites', FavoriteViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }))
]
