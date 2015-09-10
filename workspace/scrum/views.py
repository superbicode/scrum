from django.conf import settings
from django.contrib.auth import get_user_model as user_model
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from scrum.models import Task

User = user_model()

# Create your views here.
def index(request):
    #title = "Hello, world. You're at the Contacts index.. \r\n\n"
    backlog_tasks = Task.objects.filter(assigned = None)
    assigned_tasks = Task.objects.exclude(assigned = request.user)
    my_tasks = Task.objects.filter(assigned = request.user)

    template = loader.get_template('scrum/index.html')
    context = RequestContext(request, {
        'backlog_tasks_list': backlog_tasks,
        'assigned_tasks_list': assigned_tasks,
        'tasks_list': my_tasks,
    })
    return HttpResponse(template.render(context))
    
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'scrum/detail.html', {
        'task': task,
        'current_user': User,
        'status_list':Task.STATUS_CHOICES,
        })

def assign(request, task_id):
    Task.objects.filter(pk=task_id).update(assigned=request.user)
    return HttpResponseRedirect('/')
    
def status(request, task_id):
    Task.objects.filter(pk=task_id).update(status=request.POST["status_id"] )
    return HttpResponseRedirect('/')
