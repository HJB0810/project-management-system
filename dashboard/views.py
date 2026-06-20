from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task
from django.db.models import Q

@login_required
def dashboard_view(request):
    total_projects=Project.objects.filter(created_by=request.user).count()
    recent_projects=Project.objects.filter(
        Q(created_by=request.user)|
        Q(members=request.user)
    ).distinct().order_by('-created_at')[:5]
    total_tasks=Task.objects.filter(assigned_to=request.user).count()
    completed_tasks=Task.objects.filter(assigned_to=request.user,status='Completed').count()
    pending_tasks=Task.objects.filter(assigned_to=request.user).exclude(status='Completed').count()
    recent_tasks=Task.objects.filter(
        assigned_to=request.user
    ).order_by('-created_at')[:5]
    context={'total_projects':total_projects,'recent_projects':recent_projects,'total_tasks':total_tasks,'completed_tasks':completed_tasks,
             'pending_tasks':pending_tasks,'recent_tasks':recent_tasks}
    
    return render (request,'dashboard.html',context)

