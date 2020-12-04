from django.contrib.auth.models import User # 追加
from rest_framework import generics


from rest_framework import viewsets
from .serializers import UserSerializer # 追加




class UserViewset(viewsets.ModelViewSet):

    user1 = User.objects.get(id = '6')
    user1.socialaccount_set.all()
    print(user1)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer