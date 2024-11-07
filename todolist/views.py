from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TodoList
from project.models import Project
# Create your views here.



@login_required
def add(request, project_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)

    if request.method == "POST":
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            TodoList.objects.create(project=project, name=name, description=description, created_by=request.user)
            return redirect(f"/projects/{project.id}/")

    return render(request, 'todolist/add.html', {'project':project})



@login_required
def todoList(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todoList = TodoList.objects.filter(project=project).get(pk=pk)

    # print(todoList.tasks)
    return render(request, 'todolist/todolist.html', {
        'project':project,
        'todolist':todoList
    })

    # return redirect()


@login_required
def edit(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todoList = TodoList.objects.filter(project=project).get(pk=pk)

    if request.method == "POST":
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        todoList.name = name
        todoList.description = description
        todoList.save()

        return redirect(f"/projects/{project_id}/{pk}/")

    return render(request, 'todolist/edit.html', {
        'project':project,
        'todolist':todoList
    })



@login_required
def delete(request, project_id, pk):
    project = Project.objects.filter(created_by=request.user)
    todoList = TodoList.objects.filter(created_by=request.user).get(pk=pk)

    todoList.delete()
    return redirect(f"/projects/{project_id}/")




