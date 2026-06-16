from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task

@login_required
def dashboard_view(request):
    total_projects=Project.objects.filter(created_by=request.user).count()
    total_tasks=Task.objects.filter(assigned_to=request.user).count()
    completed_tasks=Task.objects.filter(assigned_to=request.user,status='Completed').count()
    context={'total_projects':total_projects,'total_tasks':total_tasks,'completed_tasks':completed_tasks}

    return render (request,'dashboard.html',context)

# Create your views here.
