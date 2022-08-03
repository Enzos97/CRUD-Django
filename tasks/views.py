from asyncio import tasks
from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request,'list_tasks.html', {"tasks": tasks})

def create_tasks(request):
    new_title = request.POST["title"]
    new_description = request.POST["description"]
    if new_title == "" or new_description == "":
        tasks = Task.objects.all()
        return render(
            request, "list_tasks.html", {"tasks": tasks, "error": "Title and description is required"}
        )
    task = Task(tittle=new_title, description=new_description)
    task.save()
    return redirect("/tasks/")
    # task = Task(tittle=request.POST['title'], description=request.POST['description'])
    # task.save()
    # return redirect('/tasks/')

def update_tasks(request, task_id):
    task = Task.objects.get(id=task_id)
    data = {'task':task} 
    # task = Task(tittle=request.PUT['title'], description=request.PUT['description'])
    print('id',task.id)
    return render(request,'update_task.html',data)

def edit_tasks(request):
    id=int(request.POST['id'])
    task = Task.objects.get(id=id)
    task.tittle=request.POST['title']
    task.description=request.POST['description']
    task.save()
    return redirect('/tasks/')

def delete_tasks(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')