from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def home(reqeust):
    return render(reqeust, 'home.html')

def add_Todo(reqeust):
    if reqeust.method == 'POST':
        name = reqeust.POST['name']
        Todo.objects.create(name=name)
    return redirect('home')

def delet_Todo(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    todo.delete()
    return redirect('home')