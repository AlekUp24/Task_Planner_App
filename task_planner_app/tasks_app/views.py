from django.shortcuts import render, redirect
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

def add_created_list(request):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        form = TaskList(name=new_name)    
        form.save()
    
    return redirect("/")

def delete_list(request,id):
    task_list = TaskList.objects.get(id=id)
    task_list.delete()

    return redirect("/")

def create_task(request,id):
    task_list = TaskList.objects.get(id=id)

    return render(request, 'create_task.html', {"list":task_list})

def add_created_task(request,id):

    if request.method == 'POST':
        list = TaskList.objects.get(id=id)
        new_name = request.POST.get('new_name')
        new_description = request.POST.get('new_description')
        new_due = request.POST.get('new_due')
        new_complete = request.POST.get('new_completed')
        
        if new_complete=="on":
            new_complete=True
        else:
            new_complete=False

        form = TaskItem(task_list = list, name = new_name, description = new_description, complete = new_complete , due_date = new_due)
        form.save()
    
    return redirect("/"+str(id))

def delete_task(request,id,id_2):
    task_item = TaskItem.objects.get(id=id_2)
    task_item.delete()

    return redirect("/"+str(id))