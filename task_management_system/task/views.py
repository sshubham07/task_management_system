from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Task,Assignment
from .serializers import TaskSerializer, AssignmentCreateSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView



# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['post']



class UserTaskViewSet(viewsets.ViewSet):
    def list(self, request, user_id=None):
        task_ids = Assignment.objects.filter(user_id=user_id).values_list('task_id', flat=True)
        tasks = Task.objects.filter(id__in=task_ids)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        assignments = serializer.save()
        return Response({"message": "Tasks assigned successfully!"}, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']






