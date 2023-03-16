from rest_framework import serializers
from .models import Project
from .models import TODO


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
