from django.contrib import admin
from .models import Task, Assignment, UserProfile
admin.site.register(Task)
admin.site.register(Assignment)
admin.site.register(UserProfile)

