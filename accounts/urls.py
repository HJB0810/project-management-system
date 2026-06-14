
from django.urls import path,include
from .views import (home_view,register_view,login_view,logout_view)

urlpatterns = [
    path('', home_view, name='home'),
    path('register/',register_view , name='register'),
    path('login/',login_view , name='login'),
    path('logout/',logout_view , name='logout')
]