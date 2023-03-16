from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import UserModelViewSet
from new_app.views import ProjectModelViewSet, TODOModelViewSet


router = DefaultRouter()
router.register('user', UserModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('TODO', TODOModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
