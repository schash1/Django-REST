from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from todo.views import UserModelViewSet, UserRetrieveAPIView, UserListAPIView
from new_app.views import ProjectModelViewSet, TODOModelViewSet, ProjectRetrieveAPIView, TODORetrieveAPIView
from new_app.views import ProjectDestroyAPIView, ProjectUpdateAPIView, TODODestroyAPIView, TODOUpdateAPIView
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView


router = DefaultRouter()
router.register('user', UserModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('TODO', TODOModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="TODO",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('generic/retrieve/<int:pk>/', UserRetrieveAPIView.as_view()),
    path('generic/retrieve/<int:pk>/', ProjectRetrieveAPIView.as_view()),
    path('generic/retrieve/<int:pk>/', TODORetrieveAPIView.as_view()),
    path('generic/destroy/<int:pk>/', ProjectDestroyAPIView.as_view()),
    path('generic/destroy/<int:pk>/', TODODestroyAPIView.as_view()),
    path('generic/update/<int:pk>/', ProjectUpdateAPIView.as_view()),
    path('generic/update/<int:pk>/', TODOUpdateAPIView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    re_path(r'^api/(?P<version>\d\.\d)/users/$', UserListAPIView.as_view()),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
