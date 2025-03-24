from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    TASK_TYPE_CHOICES = [
        ('personal', 'Personal'),
        ('work', 'Work'),
        ('study', 'Study'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    task_type = models.CharField(max_length=50, choices=TASK_TYPE_CHOICES, default='other')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.IntegerField(default=3, help_text="Priority from 1 (highest) to 5 (lowest)", validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_active = models.BooleanField(default=True)

    def mark_completed(self):
        self.status = 'completed'
        self.completed_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['priority', 'created_at']


class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_assignments')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_assignments')
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.task.name}"

    class Meta:
        unique_together = ('user', 'task')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    mobile = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

