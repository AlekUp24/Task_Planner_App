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

def task_details(request,id,id_2):
    task_list = TaskList.objects.get(id=id)
    task = TaskItem.objects.get(id=id_2)

    return render(request, 'task_details.html', {"task":task})

def create_list(request):
    return render(request, 'create_list.html', {})

def create_task(request,id):
    task_list = TaskList.objects.get(id=id)
    return render(request, 'create_task.html', {"list":task_list})


