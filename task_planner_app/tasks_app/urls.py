from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.getlist, name="get_list"),
    path('<int:id>/<int:id_2>', views.task_details, name="task_details"),
]