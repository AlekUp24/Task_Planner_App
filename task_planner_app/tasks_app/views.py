from django.shortcuts import render, redirect
from .models import TaskList, TaskItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        lists = TaskList.objects.filter(user_id=request.user.id)
        return render(request, 'index.html', {"lists":lists})
    else:
        return redirect('login')
    
# lists

def getlist(request,id):
    task_list = TaskList.objects.get(id=id)
    items = TaskItem.objects.filter(task_list__id=id)

    return render(request, 'list_details.html', {"list": task_list, "items":items})

def create_list(request):
    return render(request, 'create_list.html', {})

def add_created_list(request):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        form = TaskList(user_id = request.user.id, name=new_name)    
        form.save()
    
    return redirect("/")

def delete_list(request,id):
    task_list = TaskList.objects.get(id=id)
    task_list.delete()

    return redirect("/")

# tasks

def task_details(request,id,id_2):
    task_list = TaskList.objects.get(id=id)
    task = TaskItem.objects.get(id=id_2)

    return render(request, 'task_details.html', {"task":task})

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

def update_task(request,id,id_2):
    item_to_update = TaskItem.objects.get(id=id_2)
    if item_to_update.complete == True:
        item_to_update.complete = False 
    else:
        item_to_update.complete = True

    item_to_update.save()
    
    return redirect("/"+str(id) + "/" + str(id_2))

def save_updated_task():
    pass


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            messages.success(request,("You have been logged in!"))
            return redirect('index')
        else:
            messages.error(request,("There was an error, please try again..."))
            return redirect('login')
    else:   
        return render(request, 'login.html',{})

def logout_user(request):
    
    logout(request)
    messages.success(request,("You have been logged out..."))

    return redirect('login')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("You have been registered successfuly! Enjoy!"))
            return redirect('index')
        else:
            messages.error(request,("Oops! There was a problem, please try again..."))
            return redirect('register')
    else:
        return render(request, 'register.html',{
            'form':form
            })