from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def add_Todo(reqeust):
    if reqeust.method == 'POST':
        name = reqeust.POST['name']
        Todo.objects.create(name=name)
    return redirect('todo_list')

def delet_Todo(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    return redirect('todo_list')

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})
