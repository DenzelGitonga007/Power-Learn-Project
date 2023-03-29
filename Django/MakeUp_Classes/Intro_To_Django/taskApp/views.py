from django.shortcuts import render
from . models import Task

# Create your views here.
def taskList(request):
    tasks = Task.objects.all()
    context = {
        "tasks" : tasks
    }
    return render(request, "tasks/tasklist.html", context)

# View task by ID
def taskDetail(request, pk):
    specific_task = Task.objects.get(pk=pk)
    context = {
        "task" : specific_task
    }
    return render(request, "tasks/taskdetail.html", context)