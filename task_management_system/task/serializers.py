from .models import Assignment
from rest_framework import serializers
from .models import Task, Assignment
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class AssignmentCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    task_id = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), write_only=True)

    class Meta:
        model = Assignment
        fields = ['user_id', 'task_id', 'assigned_at']

    def create(self, validated_data):
        user = validated_data['user_id']
        task = validated_data['task_id']
        assignment, created = Assignment.objects.get_or_create(user=user, task=task)
        return assignment

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

