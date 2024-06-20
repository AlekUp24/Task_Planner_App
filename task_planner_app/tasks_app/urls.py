from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.getlist, name="get_list"),
    path('<int:id>/<int:id_2>', views.task_details, name="task_details"),
    path('create_list', views.create_list, name="create_list"),
    path('add_created_list', views.add_created_list, name="add_create_list"),
    path('<int:id>/create_task', views.create_task,  name="create_task"),
    path('<int:id>/delete_list', views.delete_list,  name="delete_list"),
    path('<int:id>/add_created_task', views.add_created_task,  name="add_created_task"),
    path('<int:id>/<int:id_2>/delete_task', views.delete_task,  name="delete_task"),
]