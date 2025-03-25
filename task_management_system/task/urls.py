from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, UserTaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'user-tasks/(?P<user_id>\d+)', UserTaskViewSet, basename='user-tasks')



urlpatterns = [
    path('api/', include(router.urls)),
]