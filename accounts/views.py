from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task
from .forms import EditProfile

def register_view(request):
   if request.method == "POST":
       form =RegisterForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(
               request,
               "Account created Successfully!"
               )
           return redirect('login')
       else:
           messages.error(request,"Invalid form data")
   else:
         form =RegisterForm()
   return render(request,'register.html',
                     {'form':form}
                     )

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(
                request,
                f"Welcome {user.username}"
            )
            return redirect('dashboard')
    else:
          form = AuthenticationForm()

    return render(
        request,
        'login.html',
        {'form': form}
    )

def logout_view(request):
    logout(request)
    return render(request,'landing.html')


def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,'landing.html')

@login_required
def profile_view(request):
    total_projects=Project.objects.filter(created_by=request.user).count()
    total_tasks=Task.objects.filter(assigned_to=request.user).count()
    completed_tasks=Task.objects.filter(assigned_to=request.user,status='Completed').count()
    context={'total_projects':total_projects,'total_tasks':total_tasks,'completed_tasks':completed_tasks,}

    
    return render (request,'profile.html',context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form =EditProfile(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Profile updated successfully!")
            return redirect('profile')
    else:
        form=EditProfile(
            instance=request.user
        )
    return render(request,'edit_profile.html',{'form':form})

