from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from todolist.models import TodoList
from project.models import Project
from .models import Task
# Create your views here.


@login_required
def add(request, project_id, todolist_id):

    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todoList = TodoList.objects.filter(project_id=project_id).get(pk=todolist_id)

    if request.method == "POST":
        name =request.POST.get('name', '')
        description = request.POST.get('description', '')
        task = Task.objects.create(project=project, todolist =todoList, name=name, description=description, 
                                   created_by=request.user)
        return redirect(f"/projects/{project_id}/{todolist_id}/")
    return render(request, 'task/add.html')



@login_required
def detail(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todoList = TodoList.objects.filter(project_id=project_id).get(pk=todolist_id)
    task = Task.objects.filter(project_id=project_id).filter(todolist_id=todolist_id).get(pk=pk)


    if request.GET.get('is_done', '') == 'yes':
        task.is_done = True
        task.save()

    return render(request, 'task/detail.html', {
        'project':project,
        'todolist':todoList,
        'task':task,
    })



@login_required
def edit(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todoList = TodoList.objects.filter(project_id=project_id).get(pk=todolist_id)
    task = Task.objects.filter(project_id=project_id).filter(todolist_id=todolist_id).get(pk=pk)

    if request.method == "POST":
        name =request.POST.get('name', '')
        description = request.POST.get('description', '')

        if task.name:
            task.name = name
        task.description = description
        task.save()

        return redirect(f"/projects/{project_id}/{todolist_id}/{pk}/")
    return render(request, 'task/edit.html',  {
        'task':task
    })




@login_required
def delete(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todoList = TodoList.objects.filter(project_id=project_id).get(pk=todolist_id)
    task = Task.objects.filter(project_id=project_id).filter(todolist_id=todolist_id).get(pk=pk)
    task.delete()

    return redirect(f"/projects/{project_id}/{todolist_id}/")