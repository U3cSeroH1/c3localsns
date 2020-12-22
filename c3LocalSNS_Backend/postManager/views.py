from rest_framework import generics
from .models import Post, Favorite
from .serializers import PostSerializer, FavoriteSerializer


from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework import viewsets

from notification.notification import NotificationChannelGroup, send_notification

#なんかでてるけど気にすんな　実行ディレクトリがルートディレクトリになってるから底と同じ場所にあるフォルダを参照しているだけ　ちゃんと動く
from permissionsSet.permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.order_by("-id")
    serializer_class = PostSerializer

    # For Notification
    def perform_create(self, serializer):
        send_notification(NotificationChannelGroup.POST, serializer.validated_data)
        super().perform_create(serializer)


class PostListAPIView(generics.ListAPIView):
    """投稿モデルの取得（一覧）APIクラス"""
    #permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.order_by("-id")
    serializer_class = PostSerializer



class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """投稿モデルの取得（一覧）APIクラス"""
    #permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer    

class PostCreateAPIView(generics.ListCreateAPIView):
    """投稿モデルの取得（一覧）APIクラス"""
    #permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.order_by("-id")
    serializer_class = FavoriteSerializer

    # For Notification
    def perform_create(self, serializer):
        send_notification(NotificationChannelGroup.FAVORITE, serializer.validated_data)
        super().perform_create(serializer)
