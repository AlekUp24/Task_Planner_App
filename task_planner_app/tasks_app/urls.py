from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.getlist, name="get_list"),
]