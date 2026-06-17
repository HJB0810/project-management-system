from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from django.db.models import Q

# Create your views here.
@login_required
def project_list(request):
    projects = Project.objects.filter(
        Q(created_by=request.user)  |
        Q(members=request.user)
    ).distinct()
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
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')

    return render(request,'project_erase.html',{'project': project})

@login_required
def project_detail(request,pk):
    project=get_object_or_404(Project,pk=pk)
    tasks=project.tasks.all()
    return render(request,'project_details.html',
                  {'project':project,'tasks':tasks})