from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Task
from django.http import Http404
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'tasks/login.html')

def detail(request, taskId):
    task = get_object_or_404(Task, pk = taskId)
    return render(request, 'tasks/detail.html', {'task': task})

@login_required
def mainTasks(request):
    tasksList = Task.objects.all()
    template = loader.get_template('tasks/feed.html')
    context = {
        'tasksList': tasksList
    }
    return render(request, 'tasks/feed.html', context)
    