from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Task,Assignment
from .serializers import TaskSerializer, AssignmentCreateSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User



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

class AssignTaskViewSet(viewsets.ViewSet):
    def create(self, request):
        user_ids = request.data.get('user_ids', [])
        task_id = request.data.get('task_id')

        if not user_ids or not task_id:
            return Response({'error': 'user_ids and task_id are required.'}, status=status.HTTP_400_BAD_REQUEST)

        task = Task.objects.filter(id=task_id).first()
        if not task:
            return Response({'error': 'Invalid task_id.'}, status=status.HTTP_404_NOT_FOUND)

        assigned_users = []
        for user_id in user_ids:
            user = User.objects.filter(id=user_id).first()
            if user:
                assignment, created = Assignment.objects.get_or_create(user=user, task=task)
                if created:
                    assigned_users.append(user.username)

        return Response({
            'message': 'Task assigned successfully.',
            'assigned_users': assigned_users
        }, status=status.HTTP_201_CREATED)






