from django.shortcuts import render

# Create your views here.
def taskList(request):
    return render(request, "tasks/tasklist.html")

# View task by ID
def taskDetail(request, pk):
    return render(request, "tasks/taskdetail.html")