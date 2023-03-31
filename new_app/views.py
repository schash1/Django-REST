from rest_framework.viewsets import ModelViewSet
from .models import Project
from .models import TODO
from rest_framework.renderers import JSONRenderer
from .serializers import ProjectModelSerializer
from .serializers import TODOModelSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .filters import ProjectFilter


class ProjectPageNumberPagination(PageNumberPagination):
    default_limit = 10


class TODOPageNumberPagination(PageNumberPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = PageNumberPagination


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    pagination_class = PageNumberPagination


class ProjectUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TODOUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class TODOListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class TODORetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class TODOCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class TODODestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


class ProjectCustomDjangoFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter


class TODODjangoFilterViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    filterset_fields = ['project', 'text', 'date_created', 'date_update', 'user', 'on_off']
    