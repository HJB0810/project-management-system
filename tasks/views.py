from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import Task_Form
from django.db.models import Q
# Create your views here.
# 
@login_required
def task_list(request):
    tasks=Task.objects.filter(assigned_to=request.user)
    search=request.GET.get('search')
    if search:
        tasks=tasks.filter(
            Q(title__icontains=search)|
            Q(description__icontains=search)
        )
    return render(request,'task_list.html',{'tasks':tasks})

@login_required
def task_create(request):
    if request.method=='POST':
        form=Task_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=Task_Form()
    return render(request,'task_form.html',{'form':form})

@login_required
def task_update(request, pk):
    task = get_object_or_404( Task,pk=pk,assigned_to=request.user)
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
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request,'task_erase.html',{'task': task})
