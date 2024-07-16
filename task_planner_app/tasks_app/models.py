from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)


class TaskItem(models.Model):
    task_list   = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100)
    complete    = models.BooleanField(default=False)
    due_date    = models.DateTimeField()