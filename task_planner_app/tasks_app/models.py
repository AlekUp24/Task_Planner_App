from django.db import models

# Create your models here.


class TaskList(models.Model):
    name = models.CharField(max_length=100)


class TaskItem(models.Model):
    task_list   = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    name        = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100)
    complete    = models.BooleanField(default=False)
    due_date    = models.DateTimeField()