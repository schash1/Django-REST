from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import UserModelViewSet, UserRetrieveAPIView
from new_app.views import ProjectModelViewSet, TODOModelViewSet, ProjectRetrieveAPIView, TODORetrieveAPIView
from new_app.views import ProjectDestroyAPIView, ProjectUpdateAPIView, TODODestroyAPIView, TODOUpdateAPIView
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('user', UserModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('TODO', TODOModelViewSet)

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
    path('api-token-auth/', views.obtain_auth_token)
]
