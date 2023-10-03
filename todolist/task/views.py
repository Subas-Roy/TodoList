from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm


# Create your views here.

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    
    return render(request, 'add_task.html', {'form': form})


def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})


def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    task.delete()
    return redirect('show_tasks')


def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    
    if request.method == 'POST':
        task.taskTitle = request.POST['taskTitle']
        task.taskDescription = request.POST['taskDescription']
        task.is_completed = 'is_completed' in request.POST
        task.save()
        return redirect('show_tasks')
    
    return render(request, 'edit_task.html', {'task': task})


def complete_task(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)
    
    if task.is_completed:
        return redirect('show_tasks')  
    
    task.is_completed = True
    task.save()
    return redirect('completed_tasks') 


def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})