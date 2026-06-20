from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import Task_Form
from projects.models import Project
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User


@login_required
def task_list(request):
    tasks=Task.objects.filter(assigned_to=request.user
    ).order_by('-created_at')
    search=request.GET.get('search')
    if search:
        tasks=tasks.filter(
            Q(title__icontains=search)|
            Q(description__icontains=search)
        )
    status=request.GET.get('status')
    if status:
        tasks=tasks.filter(status=status)
    paginator=Paginator(tasks,5)
    page_number=request.GET.get('page')
    tasks=paginator.get_page(page_number)
    return render(request,'task_list.html',{'tasks':tasks})

@login_required
def task_create(request):
    projects=Project.objects.filter(
        Q(created_by=request.user) |
        Q(members=request.user)
    ).distinct()
    if not projects.exists():
        messages.error(request,"You are not a member of any project.")
        return redirect('task_list')
    if request.method=='POST':
        form=Task_Form(request.POST,user=request.user)
        if form.is_valid():
            task =form.save(commit=False)
            if (task.assigned_to != task.project.created_by
                and task.assigned_to not in task.project.members.all()
            ):
                messages.error(request,"Selected user is not a member of this project."
                )
                return render (request,'task_form.html',{'form':form}
                               )
            task.save()
            messages.success(request,"Task created succesfully.")
            return redirect('task_list')
    else:
            form=Task_Form(user=request.user)
    return render(request,'task_form.html',
                      {'form':form})

@login_required
def task_update(request, pk):
    task = get_object_or_404( Task,pk=pk,assigned_to=request.user)
    if (request.user !=task.assigned_to 
    and 
    request.user !=task.project.created_by):
        return HttpResponseForbidden(
            "You are not allowed to edit this task."
        )
    if request.method == 'POST':
        form = Task_Form(request.POST,user=request.user,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = Task_Form(instance=task)

    return render(request,'task_form.html',{'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task,pk=pk,assigned_to=request.user)
    if request.user != Task.project.created_by:
        return HttpResponseForbidden(
            "Only project manager can delete task."
        )
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request,'task_erase.html',{'task': task})


@login_required
def get_project_members(request,project_id):
    project=get_object_or_404(Project,id=project_id)
    members =list(project.members.values('id','username'))
    owner={'id':project.created_by.id,
            'username':project.created_by.username}
    members.append(owner)
    return JsonResponse(
        members,safe=False
    )