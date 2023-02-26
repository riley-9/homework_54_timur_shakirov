from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Task
from webapp.forms import TaskForm


def index_view(request: WSGIRequest):
    task_list = Task.objects.all()
    if task_list:
        context = {'task_list': task_list}
        return render(request, 'index.html', context=context)
    else:
        return render(request, 'index.html')


def create_task(request: WSGIRequest):
    form = TaskForm(data=request.POST)
    if request.method == 'GET':
        context = {'statuses': Task.STATUSES, 'form': form}
        return render(request, 'add_task.html', context=context)
    elif request.method == 'POST':
        if form.is_valid():
            task = form.save()
            return redirect('detail', pk=task.pk)


def task_detail(request: WSGIRequest, pk):
    context = {'task': get_object_or_404(Task, pk=pk)}
    return render(request, 'task_detail.html', context=context)


def update_task(request: WSGIRequest, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)
    if request.method == 'GET':
        context = {
            'task': task,
            'form': form
        }
        return render(request, 'update_task.html', context=context)
    elif request.method == 'POST':
        if form.is_valid():
            task = form.save()
            return redirect('detail', pk=task.pk)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
