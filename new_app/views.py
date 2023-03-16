from rest_framework.viewsets import ModelViewSet
from .models import Project
from .models import TODO
from .serializers import ProjectModelSerializer
from .serializers import TODOModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
