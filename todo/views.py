from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from .models import User
from .serializers import UserModelSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import UpdateAPIView, ListAPIView, RetrieveAPIView


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = PageNumberPagination


class UserUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
