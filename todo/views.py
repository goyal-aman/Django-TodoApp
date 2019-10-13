from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.
def home(request):
    all_todo = Todo.objects.all().order_by('-pk')
    context = {
        'all_todo':all_todo
    }
    return render(request, 'todo/home.html', context)

def addTodo(request):
    todo_obj = request.POST['content']
    print(f'this is aman {todo_obj}')
    if todo_obj != '':
        Todo(content=todo_obj).save()
    return redirect('home')

def deleteTodo(request, item_id):
    todo_item = Todo.objects.get(pk=item_id)
    todo_item.delete()
    return redirect('home')
def editTodo(request, item_id):
    todo_item = Todo.objects.get(pk=item_id)
    