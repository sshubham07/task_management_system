from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, UserTaskViewSet, AssignmentViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'user-tasks/(?P<user_id>\d+)', UserTaskViewSet, basename='user-tasks')
router.register(r'assign-task', AssignmentViewSet, basename='assign-task')
router.register(r'register', UserViewSet, basename='user')




urlpatterns = [
    path('api/', include(router.urls)),
]