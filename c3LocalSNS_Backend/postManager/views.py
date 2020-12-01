from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

from rest_framework import viewsets

#なんかでてるけど気にすんな　実行ディレクトリがルートディレクトリになってるから底と同じ場所にあるフォルダを参照しているだけ　ちゃんと動く
from permissionsSet.permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListAPIView(generics.ListAPIView):
    """投稿モデルの取得（一覧）APIクラス"""
    #permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
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