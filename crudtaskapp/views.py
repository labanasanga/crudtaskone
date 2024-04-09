from django.shortcuts import render,redirect,get_object_or_404

from .forms import TaskForm
from .models import Task
from crudtaskapp.models import Task



# Create your views here.
def task_list(request):
    tasks=Task.objects.all()

    return render(request,"task_list.html",{"tasks":tasks})

def task_detail(request,id):
    task = get_object_or_404(Task,id=id)
    return render(request,"task_details.html",{"task":task})
def create_task(request):
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('')
    else:
        form = TaskForm()
        return render(request,"task_forms.html",{"form":form})
def edit_task(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method=="POST":
        form = TaskForm(request,request.POST,instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm(request,instance=task)
        return render(request,"task_forms.html",{"form":form})
        task.delete()
        return redirect('')
    return render(request,"edit_task.html",{"task":task})

