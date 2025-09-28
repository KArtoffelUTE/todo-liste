from . import views

from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('delete_todo/<int:todo_id>/', views.delet_Todo, name='delete_todo'),
    path('add_todo/', views.add_Todo, name='add_todo'),
] 