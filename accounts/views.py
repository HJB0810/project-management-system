from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

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
           print(form.errors)
   else:
         form =RegisterForm()
   return render(request,'register.html',
                     {'form':form}
                     )

def login_view(request):
   # if request.user.is_authenticated:
    #    return redirect('dashboard')
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