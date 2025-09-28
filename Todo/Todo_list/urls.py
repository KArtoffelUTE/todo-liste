from . import views

from django.urls import path

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('delete/<int:todo_id>/', views.delet_Todo, name='delete_todo'),
    path('add/', views.add_Todo, name='add_todo'),
] 