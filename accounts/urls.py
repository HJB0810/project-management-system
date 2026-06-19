
from django.urls import path,include
from .views import (home_view,register_view,login_view,
                    logout_view,profile_view,edit_profile)
from django.contrib.auth.views import ( PasswordChangeView, PasswordChangeDoneView )

urlpatterns = [
    path('',home_view,name='home'),
    path('register/',register_view , name='register'),
    path('login/',login_view , name='login'),
    path('logout/',logout_view , name='logout'),
    path('profile/',profile_view,name='profile'),
    path('profile/edit/',edit_profile,name='edit_profile'),
    path('password-change/',PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
]