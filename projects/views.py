from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from django.db.models import Q
from django.db.models import Count
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden


@login_required
def project_list(request):
    projects = Project.objects.filter(
        Q(created_by=request.user)  |
        Q(members=request.user)
    ).distinct().order_by('-created_at')
    search=request.GET.get('search')
    if search:
        projects=projects.filter(
            Q(name__icontains=search)|
            Q(description__icontains=search)
        )
    paginator=Paginator(projects,5)
    page_number=request.GET.get('page')
    projects=paginator.get_page(page_number)

    return render(request,'project.html',{'projects':projects})

@login_required
def project_create(request):
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.created_by =request.user
            project.save()

            form.save_m2m()
            return redirect('project_list')
    else:
        form= ProjectForm()
    return render(request,'projectForm.html',{'form':form})


@login_required
def project_update(request, pk):
    project = get_object_or_404( Project,pk=pk,created_by=request.user)
    if request.user !=project.created_by:
        return HttpResponseForbidden(
            "You are not allowed to edit this project."
        )
    if request.method == 'POST':
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)

    return render(request,'projectForm.html',{'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project,pk=pk,created_by=request.user)
    if request.user != project.created_by:
        return HttpResponseForbidden(
            "You are not allowed to delete this project."
        )
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')

    return render(request,'project_erase.html',{'project': project})

@login_required
def project_detail(request,pk):
    project=get_object_or_404(Project,pk=pk)
    if (request.user != project.created_by 
        and
        request.user not in project.members.all()
        ):
        return HttpResponseForbidden("You are not a member of this project.")
    tasks=project.tasks.all()
    total_tasks=tasks.count()
    completed_tasks=tasks.filter(status='Completed').count()
    if total_tasks>0:
        progress=int((completed_tasks/total_tasks)*100)
    else: 
        progress=0
    
    return render(request,'project_details.html',
                  {'project':project,'tasks':tasks,'progress':progress})

