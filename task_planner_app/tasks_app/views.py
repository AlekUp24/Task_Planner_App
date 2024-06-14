from django.shortcuts import render
from .models import TaskList, TaskItem
# Create your views here.

def index(request):
    lists = TaskList.objects.all()

    return render(request, 'index.html', {"lists":lists})

def getlist(request,id):
    task_list = TaskList.objects.get(id=id)
    items = TaskItem.objects.filter(task_list__id=id)

    return render(request, 'list_details.html', {"list": task_list, "items":items})