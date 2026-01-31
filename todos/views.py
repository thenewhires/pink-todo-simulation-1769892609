from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.http import HttpResponse

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Todo.objects.create(text=text)
    return redirect('todo_list')


def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.completed = True  # Bug: Sets completed to True, but doesn't save
    return redirect('todo_list')


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todo_list')
