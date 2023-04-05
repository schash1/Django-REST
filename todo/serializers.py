from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'login', 'password')


class UserFullModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'